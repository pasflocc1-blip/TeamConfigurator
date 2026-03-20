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

        <div class="status-badge" :class="data.status">
          {{ data.status === 'ok' ? '✅ Database operativo' : '❌ Errore' }}
        </div>

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
            <span v-for="t in data.tables" :key="t" class="table-badge">{{ t }}</span>
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

        <!-- Azioni -->
        <div class="modal-actions">
          <button @click="load" class="btn-reload">↻ Aggiorna</button>
          <button @click="confirmReset = 'teams'" class="btn-reset">🗑️ Svuota squadre</button>
          <button @click="confirmReset = 'all'" class="btn-reset-all">⚠️ Svuota tutto</button>
        </div>

        <!-- Conferma reset squadre -->
        <div v-if="confirmReset === 'teams'" class="confirm-box">
          <div style="color:white; margin-bottom:10px">
            ⚠️ Verranno eliminate tutte le <strong>{{ data.teams_count }} squadre</strong>.<br>
            <small style="color:#94a3b8">L'anagrafica calciatori rimarrà intatta.</small>
          </div>
          <div style="display:flex; gap:8px">
            <button @click="confirmReset = null" class="btn-cancel-small">Annulla</button>
            <button @click="resetTeams" class="btn-confirm-reset">Sì, elimina squadre</button>
          </div>
        </div>

        <!-- Conferma reset tutto -->
        <div v-if="confirmReset === 'all'" class="confirm-box danger">
          <div style="color:white; margin-bottom:10px">
            ⚠️ Verranno eliminati <strong>tutti i dati</strong> inclusa l'anagrafica.<br>
            <small style="color:#fca5a5">Questa operazione non è reversibile!</small>
          </div>
          <div style="display:flex; gap:8px">
            <button @click="confirmReset = null" class="btn-cancel-small">Annulla</button>
            <button @click="resetAll" class="btn-confirm-reset">Sì, svuota tutto</button>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '@/services/api'

defineEmits(['close'])

const loading      = ref(true)
const error        = ref(null)
const data         = ref(null)
const confirmReset = ref(null)

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
    error.value = e.response?.data?.detail || 'Errore di connessione al backend'
  } finally {
    loading.value = false
  }
}

const resetTeams = async () => {
  try {
    await api.delete('/debug/db/reset')
    confirmReset.value = null
    await load()
  } catch { error.value = 'Errore durante il reset' }
}

const resetAll = async () => {
  try {
    await api.delete('/debug/db/reset-all')
    confirmReset.value = null
    await load()
  } catch { error.value = 'Errore durante il reset completo' }
}

onMounted(load)
</script>

<style scoped>
.modal-overlay { position: fixed; inset: 0; background: rgba(0,0,0,0.75); z-index: 300; display: flex; align-items: center; justify-content: center; padding: 16px; }
.modal { background: #0f172a; border: 1px solid #334155; border-radius: 16px; width: 100%; max-width: 560px; max-height: 88vh; display: flex; flex-direction: column; overflow: hidden; }
.modal-header { display: flex; justify-content: space-between; align-items: center; padding: 16px 20px; border-bottom: 1px solid #1e293b; font-weight: 700; font-size: 15px; color: white; }
.modal-close { background: none; border: none; color: #64748b; cursor: pointer; font-size: 22px; }
.modal-body { padding: 16px 20px; overflow-y: auto; flex: 1; display: flex; flex-direction: column; gap: 14px; }
.modal-body.center { align-items: center; justify-content: center; min-height: 200px; }
.spinner { width: 36px; height: 36px; border: 3px solid #334155; border-top-color: #22c55e; border-radius: 50%; animation: spin 0.8s linear infinite; }
@keyframes spin { to { transform: rotate(360deg); } }
.status-badge { padding: 8px 16px; border-radius: 8px; font-weight: 700; font-size: 14px; text-align: center; }
.status-badge.ok { background: #14532d; color: #86efac; }
.info-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; }
.info-card { background: #1e293b; border-radius: 10px; padding: 14px; text-align: center; border: 1px solid #334155; }
.info-value { font-size: 24px; font-weight: 800; color: #22c55e; }
.info-label { font-size: 11px; color: #64748b; margin-top: 4px; text-transform: uppercase; }
.info-row { display: flex; gap: 12px; align-items: flex-start; background: #1e293b; border-radius: 8px; padding: 10px 14px; }
.info-row-label { font-size: 11px; color: #64748b; text-transform: uppercase; font-weight: 600; flex-shrink: 0; padding-top: 2px; }
.info-row-value { color: white; font-size: 13px; flex: 1; word-break: break-all; }
.info-row-value.path { font-family: monospace; font-size: 11px; color: #94a3b8; }
.table-badge { display: inline-block; background: #334155; border-radius: 4px; padding: 2px 8px; font-size: 12px; color: #94a3b8; margin-right: 6px; }
.section-title { font-size: 11px; color: #64748b; text-transform: uppercase; font-weight: 600; }
.team-list { background: #1e293b; border-radius: 8px; overflow: hidden; border: 1px solid #334155; }
.team-row { display: flex; align-items: center; gap: 10px; padding: 8px 14px; border-bottom: 1px solid #0f172a; font-size: 13px; }
.team-row:last-child { border-bottom: none; }
.team-name { color: white; font-weight: 600; flex: 1; }
.team-formation { color: #22c55e; font-weight: 700; font-size: 12px; }
.team-players { color: #64748b; font-size: 11px; }
.team-date { color: #475569; font-size: 11px; }
.empty-teams { background: #1e293b; border-radius: 8px; padding: 20px; text-align: center; color: #475569; font-size: 13px; border: 1px solid #334155; }
.modal-actions { display: flex; gap: 8px; }
.btn-reload { flex: 1; background: #1e293b; border: 1px solid #334155; border-radius: 8px; padding: 10px; color: #94a3b8; cursor: pointer; font-size: 13px; font-weight: 600; }
.btn-reload:hover { background: #334155; }
.btn-reset { flex: 1; background: #450a0a; border: 1px solid #7f1d1d; border-radius: 8px; padding: 10px; color: #ef4444; cursor: pointer; font-size: 12px; font-weight: 600; }
.btn-reset-all { flex: 1; background: #1c1917; border: 1px solid #78350f; border-radius: 8px; padding: 10px; color: #f59e0b; cursor: pointer; font-size: 12px; font-weight: 600; }
.confirm-box { background: #1c1917; border: 1px solid #ef4444; border-radius: 8px; padding: 14px; }
.confirm-box.danger { border-color: #f59e0b; }
.btn-cancel-small { flex: 1; background: #334155; border: none; border-radius: 6px; padding: 9px; color: #94a3b8; cursor: pointer; font-size: 13px; }
.btn-confirm-reset { flex: 1; background: #ef4444; border: none; border-radius: 6px; padding: 9px; color: white; font-weight: 700; cursor: pointer; font-size: 13px; }
</style>