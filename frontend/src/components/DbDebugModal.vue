<template>
  <div class="modal-overlay" @click.self="$emit('close')">
    <div class="modal">
      <div class="modal-header">
        <span>🗄️ Stato Database</span>
        <button @click="$emit('close')" class="modal-close">×</button>
      </div>

      <div v-if="loading" class="modal-body center">
        <div class="spinner" />
        <div style="color:#64748b; margin-top:12px">Lettura database...</div>
      </div>

      <div v-else-if="error" class="modal-body center">
        <div style="font-size:36px">❌</div>
        <div style="color:#ef4444; margin-top:8px">{{ error }}</div>
        <button @click="load" class="btn-reload">↻ Riprova</button>
      </div>

      <div v-else-if="data" class="modal-body">

        <!-- Status -->
        <div class="status-badge ok">✅ Database operativo</div>

        <!-- Contatori -->
        <div class="info-grid">
          <div class="info-card">
            <div class="info-value">{{ data.teams_count }}</div>
            <div class="info-label">Squadre</div>
          </div>
          <div class="info-card">
            <div class="info-value">{{ data.registry_count }}</div>
            <div class="info-label">Anagrafica</div>
          </div>
          <div class="info-card">
            <div class="info-value">{{ data.db_size_kb }} KB</div>
            <div class="info-label">Dimensione</div>
          </div>
        </div>

        <!-- Percorso -->
        <div class="info-row">
          <span class="info-row-label">Percorso DB</span>
          <span class="info-row-value path">{{ data.db_path }}</span>
        </div>

        <!-- Tabelle -->
        <div class="info-row">
          <span class="info-row-label">Tabelle</span>
          <span class="info-row-value">
            <span
              v-for="t in data.tables" :key="t"
              class="table-badge"
              :class="{ active: quickQuery === t }"
              @click="setQuickQuery(t)"
              title="Clicca per fare SELECT"
            >{{ t }}</span>
          </span>
        </div>

        <!-- Ultime squadre -->
        <div v-if="data.last_teams.length > 0">
          <div class="section-title">Ultime squadre salvate</div>
          <div class="team-list">
            <div v-for="t in data.last_teams" :key="t.id" class="team-row">
              <span class="team-name">{{ t.name }}</span>
              <span class="team-formation">{{ t.formation }}</span>
              <span class="team-players">{{ t.players }} pos.</span>
              <span class="team-date">{{ formatDate(t.updated_at) }}</span>
            </div>
          </div>
        </div>
        <div v-else class="empty-teams">Nessuna squadra nel database</div>

        <!-- ── SQL Query ── -->
        <div class="section-title">🔍 Query SQL</div>
        <div class="query-box">
          <div class="query-shortcuts">
            <button @click="setQuickQuery('teams')" class="shortcut-btn">teams</button>
            <button @click="setQuickQuery('players')" class="shortcut-btn">players</button>
            <button @click="setQuickQuery('registry_players')" class="shortcut-btn">registry_players</button>
            <button @click="sql = 'SELECT COUNT(*) as totale, role FROM registry_players GROUP BY role ORDER BY totale DESC'" class="shortcut-btn">per ruolo</button>
            <button @click="sql = 'SELECT COUNT(*) as totale, team_name FROM registry_players GROUP BY team_name ORDER BY team_name'" class="shortcut-btn">per squadra</button>
            <button @click="sql = squadreQuery" class="shortcut-btn shortcut-special">🏟️ squadre + giocatori</button>
            <button @click="sql = squadreRiepilogoQuery" class="shortcut-btn shortcut-special">📋 riepilogo squadre</button>
          </div>
          <textarea
            v-model="sql"
            class="sql-input"
            placeholder="SELECT * FROM registry_players LIMIT 10"
            rows="3"
            @keydown.ctrl.enter="runQuery"
          />
          <div style="display:flex; justify-content:space-between; align-items:center">
            <span style="font-size:11px; color:#475569">Ctrl+Enter per eseguire — solo SELECT permesse</span>
            <button @click="runQuery" :disabled="queryLoading" class="btn-run">
              {{ queryLoading ? '⏳' : '▶ Esegui' }}
            </button>
          </div>
        </div>


        <!-- Azioni reset -->
        <div class="modal-actions">
          <button @click="load" class="btn-reload">↻ Aggiorna</button>
          <button @click="confirmReset = 'teams'" class="btn-reset">🗑️ Svuota squadre</button>
          <button @click="confirmReset = 'all'" class="btn-reset-all">⚠️ Svuota tutto</button>
        </div>

        <div v-if="confirmReset === 'teams'" class="confirm-box">
          <div style="color:white; margin-bottom:10px">
            ⚠️ Verranno eliminate tutte le <strong>{{ data.teams_count }} squadre</strong>.<br>
            <small style="color:#94a3b8">L'anagrafica rimarrà intatta.</small>
          </div>
          <div style="display:flex; gap:8px">
            <button @click="confirmReset = null" class="btn-cancel-small">Annulla</button>
            <button @click="resetTeams" class="btn-confirm-reset">Sì, elimina squadre</button>
          </div>
        </div>

        <div v-if="confirmReset === 'all'" class="confirm-box danger">
          <div style="color:white; margin-bottom:10px">
            ⚠️ Verranno eliminati <strong>tutti i dati</strong> inclusa l'anagrafica.<br>
            <small style="color:#fca5a5">Operazione non reversibile!</small>
          </div>
          <div style="display:flex; gap:8px">
            <button @click="confirmReset = null" class="btn-cancel-small">Annulla</button>
            <button @click="resetAll" class="btn-confirm-reset">Sì, svuota tutto</button>
          </div>
        </div>

      </div>
    </div>
  </div>
  <!-- Dialog risultati SQL -->
  <SqlResultModal
    v-if="showSqlResult && queryResult"
    :result="queryResult"
    :sql="sql"
    @close="showSqlResult = false"
  />
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '@/services/api'
import SqlResultModal from '@/components/SqlResultModal.vue'

defineEmits(['close'])

const loading      = ref(true)
const error        = ref(null)
const data         = ref(null)
const confirmReset = ref(null)
const sql          = ref('SELECT * FROM registry_players LIMIT 20')
const queryLoading = ref(false)
const queryResult  = ref(null)
const queryError   = ref(null)
const quickQuery   = ref(null)
const showSqlResult = ref(false)

// Query pronte per squadre configurate
const squadreQuery = `SELECT
  t.name           AS squadra,
  t.formation      AS modulo,
  p.position_label AS ruolo,
  CASE p.slot
    WHEN 0 THEN 'Titolare'
    WHEN 1 THEN 'Riserva 1'
    WHEN 2 THEN 'Riserva 2'
  END              AS tipo,
  p.name           AS calciatore
FROM teams t
LEFT JOIN players p ON p.team_id = t.id
ORDER BY
  t.name,
  CASE p.position_label
    WHEN 'POR'              THEN 1
    WHEN 'TD'  THEN 2  WHEN 'TS'  THEN 2 WHEN 'DC'  THEN 2
    WHEN 'TLD' THEN 2  WHEN 'TLS' THEN 2
    WHEN 'CDC' THEN 3  WHEN 'CC'  THEN 3  WHEN 'CCD' THEN 3  WHEN 'CCS' THEN 3
    WHEN 'TRQ' THEN 4  WHEN 'ALD' THEN 4  WHEN 'ALS' THEN 4  WHEN 'ATT' THEN 4
    ELSE 5
  END,
  p.slot`

const squadreRiepilogoQuery = `SELECT
  t.id        AS id,
  t.name      AS squadra,
  t.formation AS modulo,
  COUNT(CASE WHEN p.slot = 0 THEN 1 END) AS titolari,
  COUNT(CASE WHEN p.slot = 1 THEN 1 END) AS riserve_1,
  COUNT(CASE WHEN p.slot = 2 THEN 1 END) AS riserve_2,
  COUNT(p.id) AS totale_giocatori,
  t.updated_at AS ultimo_aggiornamento
FROM teams t
LEFT JOIN players p ON p.team_id = t.id
GROUP BY t.id
ORDER BY t.updated_at DESC`

const formatDate = (dt) => {
  if (!dt) return '—'
  const d = new Date(String(dt).replace(' ', 'T'))
  if (isNaN(d.getTime())) return '—'
  return d.toLocaleDateString('it-IT', {
    day: '2-digit', month: '2-digit', year: 'numeric',
    hour: '2-digit', minute: '2-digit',
  })
}

const load = async () => {
  loading.value = true
  error.value   = null
  try {
    const res  = await api.get('/debug/db')
    data.value = res.data
  } catch (e) {
    error.value = e.response?.data?.detail || 'Errore di connessione'
  } finally {
    loading.value = false
  }
}

const setQuickQuery = (table) => {
  quickQuery.value = table
  sql.value = `SELECT * FROM ${table} LIMIT 50`
}

const runQuery = async () => {
  if (!sql.value.trim()) return
  queryLoading.value = true
  queryError.value   = null
  queryResult.value  = null
  try {
    const res = await api.post('/debug/db/query', { sql: sql.value })
    queryResult.value = res.data
    showSqlResult.value = true   // apri la dialog
  } catch (e) {
    queryError.value = e.response?.data?.detail || 'Errore nella query'
  } finally {
    queryLoading.value = false
  }
}

const resetTeams = async () => {
  try {
    await api.delete('/debug/db/reset')
    confirmReset.value = null
    queryResult.value  = null
    await load()
  } catch { error.value = 'Errore reset' }
}

const resetAll = async () => {
  try {
    await api.delete('/debug/db/reset-all')
    confirmReset.value = null
    queryResult.value  = null
    await load()
  } catch { error.value = 'Errore reset completo' }
}

onMounted(load)

</script>

<style scoped>
.modal-overlay { position: fixed; inset: 0; background: rgba(0,0,0,0.75); z-index: 300; display: flex; align-items: center; justify-content: center; padding: 16px; }
.modal { background: #0f172a; border: 1px solid #334155; border-radius: 16px; width: 100%; max-width: 700px; max-height: 92vh; display: flex; flex-direction: column; overflow: hidden; }
.modal-header { display: flex; justify-content: space-between; align-items: center; padding: 16px 20px; border-bottom: 1px solid #1e293b; font-weight: 700; font-size: 15px; color: white; }
.modal-close { background: none; border: none; color: #64748b; cursor: pointer; font-size: 22px; }
.modal-body { padding: 16px 20px; overflow-y: auto; flex: 1; display: flex; flex-direction: column; gap: 14px; }
.modal-body.center { align-items: center; justify-content: center; min-height: 200px; }
.spinner { width: 36px; height: 36px; border: 3px solid #334155; border-top-color: #22c55e; border-radius: 50%; animation: spin 0.8s linear infinite; }
@keyframes spin { to { transform: rotate(360deg); } }
.status-badge.ok { background: #14532d; color: #86efac; padding: 8px 16px; border-radius: 8px; font-weight: 700; font-size: 14px; text-align: center; }
.info-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; }
.info-card { background: #1e293b; border-radius: 10px; padding: 14px; text-align: center; border: 1px solid #334155; }
.info-value { font-size: 24px; font-weight: 800; color: #22c55e; }
.info-label { font-size: 11px; color: #64748b; margin-top: 4px; text-transform: uppercase; }
.info-row { display: flex; gap: 12px; align-items: flex-start; background: #1e293b; border-radius: 8px; padding: 10px 14px; }
.info-row-label { font-size: 11px; color: #64748b; text-transform: uppercase; font-weight: 600; flex-shrink: 0; padding-top: 2px; }
.info-row-value { color: white; font-size: 13px; flex: 1; word-break: break-all; }
.info-row-value.path { font-family: monospace; font-size: 11px; color: #94a3b8; }
.table-badge { display: inline-block; background: #334155; border-radius: 4px; padding: 3px 10px; font-size: 12px; color: #94a3b8; margin-right: 6px; cursor: pointer; transition: all 0.15s; }
.table-badge:hover, .table-badge.active { background: #22c55e; color: white; }
.section-title { font-size: 11px; color: #64748b; text-transform: uppercase; font-weight: 600; }
.team-list { background: #1e293b; border-radius: 8px; overflow: hidden; border: 1px solid #334155; }
.team-row { display: flex; align-items: center; gap: 10px; padding: 8px 14px; border-bottom: 1px solid #0f172a; font-size: 13px; }
.team-row:last-child { border-bottom: none; }
.team-name { color: white; font-weight: 600; flex: 1; }
.team-formation { color: #22c55e; font-weight: 700; font-size: 12px; }
.team-players { color: #64748b; font-size: 11px; }
.team-date { color: #475569; font-size: 11px; }
.empty-teams { background: #1e293b; border-radius: 8px; padding: 20px; text-align: center; color: #475569; font-size: 13px; border: 1px solid #334155; }
/* Query */
.query-box { background: #1e293b; border-radius: 10px; padding: 12px; border: 1px solid #334155; display: flex; flex-direction: column; gap: 8px; }
.query-shortcuts { display: flex; flex-wrap: wrap; gap: 5px; }
.shortcut-btn { background: #334155; border: none; border-radius: 4px; padding: 3px 10px; color: #94a3b8; cursor: pointer; font-size: 11px; font-family: monospace; }
.shortcut-btn:hover { background: #475569; color: white; }
.shortcut-btn.shortcut-special { background: #1e3a5f; color: #93c5fd; border: 1px solid #2563eb; }
.shortcut-btn.shortcut-special:hover { background: #1e40af; color: white; }
.sql-input { background: #0f172a; border: 1px solid #334155; border-radius: 6px; padding: 10px; color: #86efac; font-size: 12px; font-family: monospace; resize: vertical; outline: none; width: 100%; box-sizing: border-box; }
.btn-run { background: #22c55e; border: none; border-radius: 6px; padding: 7px 18px; color: white; font-weight: 700; cursor: pointer; font-size: 13px; }
.btn-run:disabled { opacity: 0.6; cursor: not-allowed; }
.query-error { background: #450a0a; border: 1px solid #7f1d1d; border-radius: 8px; padding: 10px 14px; color: #ef4444; font-size: 13px; font-family: monospace; }
.query-result-box { background: #1e293b; border-radius: 8px; border: 1px solid #334155; overflow: hidden; }
.query-result-header { padding: 8px 14px; font-size: 11px; color: #64748b; border-bottom: 1px solid #0f172a; }
.query-result-scroll { overflow-x: auto; max-height: 260px; overflow-y: auto; }
.result-table { width: 100%; border-collapse: collapse; font-size: 12px; }
.result-table th { background: #0f172a; color: #64748b; padding: 6px 12px; text-align: left; font-weight: 600; text-transform: uppercase; font-size: 10px; position: sticky; top: 0; white-space: nowrap; }
.result-table td { color: #e2e8f0; padding: 6px 12px; border-bottom: 1px solid #0f172a; white-space: nowrap; }
.result-table tr:hover td { background: #0f172a; }
/* Azioni */
.modal-actions { display: flex; gap: 8px; }
.btn-reload { flex: 1; background: #1e293b; border: 1px solid #334155; border-radius: 8px; padding: 10px; color: #94a3b8; cursor: pointer; font-size: 13px; font-weight: 600; }
.btn-reset { flex: 1; background: #450a0a; border: 1px solid #7f1d1d; border-radius: 8px; padding: 10px; color: #ef4444; cursor: pointer; font-size: 12px; font-weight: 600; }
.btn-reset-all { flex: 1; background: #1c1917; border: 1px solid #78350f; border-radius: 8px; padding: 10px; color: #f59e0b; cursor: pointer; font-size: 12px; font-weight: 600; }
.confirm-box { background: #1c1917; border: 1px solid #ef4444; border-radius: 8px; padding: 14px; }
.confirm-box.danger { border-color: #f59e0b; }
.btn-cancel-small { flex: 1; background: #334155; border: none; border-radius: 6px; padding: 9px; color: #94a3b8; cursor: pointer; font-size: 13px; }
.btn-confirm-reset { flex: 1; background: #ef4444; border: none; border-radius: 6px; padding: 9px; color: white; font-weight: 700; cursor: pointer; font-size: 13px; }
</style>