<template>
  <div class="editor">

    <!-- Header -->
    <div class="header">
      <h1>⚽ Football Team Builder</h1>
      <button @click="showRegistry = true" class="btn-registry">
        📋 Anagrafica ({{ registry.length }})
      </button>
    </div>

    <!-- Tabs -->
    <div class="tabs">
      <button :class="{ active: tab === 'editor' }" @click="tab = 'editor'">🏟️ Editor</button>
      <button :class="{ active: tab === 'teams' }" @click="loadTeams(); tab = 'teams'">
        📋 Squadre ({{ savedTeams.length }})
      </button>
    </div>

    <!-- Notification -->
    <Transition name="fade">
      <div v-if="notification" :class="['notification', notification.type]">
        {{ notification.msg }}
      </div>
    </Transition>

    <!-- ── EDITOR TAB ── -->
    <div v-if="tab === 'editor'" class="editor-layout">

      <!-- Colonna sinistra: campo -->
      <div class="pitch-col">
        <div class="field-group">
          <label>Nome Squadra</label>
          <input v-model="teamName" placeholder="Es: FC Milano" class="text-input" />
        </div>

        <div class="field-group">
          <label>Modulo</label>
          <div class="formation-pills">
            <button
              v-for="(f, key) in FORMATIONS" :key="key"
              :class="{ active: formation === key }"
              @click="changeFormation(key)"
            >{{ key }}</button>
          </div>
        </div>

        <FootballPitch
          ref="pitchRef"
          :positions="currentPositions"
          :players="players"
          :selected-id="selectedPos?.id"
          @select="selectPosition"
        />
      </div>

      <!-- Colonna destra: pannello assegnazione -->
      <div class="roster-col">

        <!-- Pannello 3 slot per posizione selezionata -->
        <div v-if="selectedPos" class="player-input-box">
          <div class="role-header">
            <span class="role-badge" :style="{ background: roleColor(selectedPos.label) }">
              {{ selectedPos.label }}
            </span>
            <span class="role-label-text">{{ ROLE_LABELS[selectedPos.label] || selectedPos.label }}</span>
          </div>

          <div
            v-for="(slot, i) in ['Titolare', '1ª Riserva', '2ª Riserva']"
            :key="i"
            class="slot-row"
          >
            <span class="slot-label">{{ slot }}</span>
            <PlayerCombo
              :registry="registry"
              :model-value="getPlayer(selectedPos.id, i)"
              @update:model-value="(v) => setPlayer(selectedPos.id, i, v)"
              @add-new="(name) => onAddNew(name, i)"
            />
          </div>
        </div>

        <div v-else class="player-input-placeholder">
          👆 Tocca un rettangolo sul campo per assegnare i giocatori
        </div>

        <!-- Lista rosa -->
        <div class="roster-list">
          <div class="roster-header">
            ROSA — {{ filledCount }}/11 titolari
            <div class="progress-bar">
              <div class="progress-fill" :style="{ width: (filledCount / 11 * 100) + '%' }" />
            </div>
          </div>
          <div
            v-for="pos in currentPositions" :key="pos.id"
            class="roster-item"
            :class="{ selected: selectedPos?.id === pos.id, filled: getPlayer(pos.id, 0) }"
            @click="selectPosition(pos)"
          >
            <span class="role-tag" :style="{ color: roleColor(pos.label) }">{{ pos.label }}</span>
            <div class="roster-names">
              <span class="roster-name-starter">{{ getPlayer(pos.id, 0) || '—' }}</span>
              <span v-if="getPlayer(pos.id, 1)" class="roster-name-reserve">{{ getPlayer(pos.id, 1) }}</span>
              <span v-if="getPlayer(pos.id, 2)" class="roster-name-reserve">{{ getPlayer(pos.id, 2) }}</span>
            </div>
            <button
              v-if="getPlayer(pos.id, 0)"
              @click.stop="clearPosition(pos.id)"
              class="clear-btn"
            >×</button>
          </div>
        </div>

        <div class="actions">
          <button @click="resetForm" class="btn-secondary">🗑️ Nuova</button>
          <button @click="saveTeam" :disabled="saving" class="btn-primary">
            {{ saving ? 'Salvataggio...' : `💾 Salva (${filledCount}/11)` }}
          </button>
        </div>
        <button @click="handleExportWord" :disabled="exporting" class="btn-export">
          {{ exporting ? '⏳ Generazione...' : '📄 Esporta in Word (A4)' }}
        </button>
      </div>
    </div>

    <!-- ── TEAMS TAB ── -->
    <div v-if="tab === 'teams'" class="teams-tab">
      <div v-if="loading" class="empty-state">Caricamento...</div>
      <div v-else-if="savedTeams.length === 0" class="empty-state">
        <div class="empty-icon">📋</div>
        <div>Nessuna squadra salvata.</div>
        <div class="empty-sub">Vai in Editor e salva la prima formazione!</div>
      </div>
      <div v-else class="team-cards">
        <div v-for="team in savedTeams" :key="team.id" class="team-card">
          <div class="team-card-header">
            <div>
              <div class="team-card-name">{{ team.name }}</div>
              <div class="team-card-meta">
                Modulo: <strong>{{ team.formation }}</strong> · {{ formatDate(team.updated_at) }}
              </div>
            </div>
            <div class="team-card-actions">
              <button @click="loadTeam(team.id)" class="btn-load">Carica</button>
              <button @click="deleteTeam(team.id)" class="btn-delete">✕</button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Modals -->
    <RegistryModal
      v-if="showRegistry"
      :registry="registry"
      @close="showRegistry = false"
      @save="onRegistrySave"
    />

    <AddPlayerModal
      v-if="addingNew"
      :name="addingNew.name"
      :pos-label="addingNew.posLabel"
      @cancel="addingNew = null"
      @confirm="onConfirmAddNew"
    />
  </div>
</template>

<script setup>
import { ref, reactive, computed, onMounted } from 'vue'
import FootballPitch from '@/components/FootballPitch.vue'
import PlayerCombo from '@/components/PlayerCombo.vue'
import RegistryModal from '@/components/RegistryModal.vue'
import AddPlayerModal from '@/components/AddPlayerModal.vue'
import { FORMATIONS, ROLE_COLORS, ROLE_LABELS } from '@/composables/useFormations'
import { teamsApi } from '@/services/api'
import { exportToWord } from '@/composables/useWordExport'

// ── State ───────────────────────────────────────────────
const tab        = ref('editor')
const teamId     = ref(null)
const teamName   = ref('')
const formation  = ref('4-3-3')
// players: { posId: ['titolare', 'riserva1', 'riserva2'] }
const players    = reactive({})
const selectedPos = ref(null)
const savedTeams = ref([])
const loading    = ref(false)
const saving     = ref(false)
const notification = ref(null)
const showRegistry = ref(false)
const addingNew  = ref(null) // { name, posId, slotIndex, posLabel }
const pitchRef   = ref(null)
const exporting  = ref(false)

const registry = ref([
  // 🇮🇹 Italiani
  { id: 1,  name: 'Donnarumma',      role: 'POR', number: 1,  birthYear: 1999, nationality: 'Italia' },
  { id: 2,  name: 'Di Lorenzo',      role: 'TD',  number: 2,  birthYear: 1988, nationality: 'Italia' },
  { id: 3,  name: 'Bastoni',         role: 'DC',  number: 23, birthYear: 1999, nationality: 'Italia' },
  { id: 4,  name: 'Bonucci',         role: 'DC',  number: 19, birthYear: 1987, nationality: 'Italia' },
  { id: 5,  name: 'Acerbi',          role: 'DC',  number: 15, birthYear: 1988, nationality: 'Italia' },
  { id: 6,  name: 'Mancini',         role: 'DC',  number: 23, birthYear: 1996, nationality: 'Italia' },
  { id: 7,  name: 'Spinazzola',      role: 'TS',  number: 4,  birthYear: 1993, nationality: 'Italia' },
  { id: 8,  name: 'Dimarco',         role: 'TS',  number: 3,  birthYear: 1997, nationality: 'Italia' },
  { id: 9,  name: 'Barella',         role: 'CC',  number: 8,  birthYear: 1997, nationality: 'Italia' },
  { id: 10, name: 'Pellegrini',      role: 'TRQ', number: 20, birthYear: 1999, nationality: 'Italia' },
  { id: 11, name: 'Verratti',        role: 'CDC', number: 6,  birthYear: 1992, nationality: 'Italia' },
  { id: 12, name: 'Jorginho',        role: 'CDC', number: 13, birthYear: 1991, nationality: 'Italia' },
  { id: 13, name: 'Tonali',          role: 'CC',  number: 8,  birthYear: 2000, nationality: 'Italia' },
  { id: 14, name: 'Frattesi',        role: 'CC',  number: 16, birthYear: 1999, nationality: 'Italia' },
  { id: 15, name: 'Chiesa',          role: 'ALD', number: 11, birthYear: 1997, nationality: 'Italia' },
  { id: 16, name: 'Raspadori',       role: 'ATT', number: 18, birthYear: 2000, nationality: 'Italia' },
  { id: 17, name: 'Immobile',        role: 'ATT', number: 17, birthYear: 1990, nationality: 'Italia' },
  { id: 18, name: 'Retegui',         role: 'ATT', number: 9,  birthYear: 2001, nationality: 'Italia' },
  { id: 19, name: 'Meret',           role: 'POR', number: 16, birthYear: 1997, nationality: 'Italia' },
  { id: 20, name: 'Vicario',         role: 'POR', number: 1,  birthYear: 1996, nationality: 'Italia' },
  // 🇪🇸 Spagnoli
  { id: 21, name: 'Ter Stegen',      role: 'POR', number: 1,  birthYear: 1992, nationality: 'Germania' },
  { id: 22, name: 'Carvajal',        role: 'TD',  number: 2,  birthYear: 1992, nationality: 'Spagna' },
  { id: 23, name: 'Militao',         role: 'DC',  number: 3,  birthYear: 1998, nationality: 'Brasile' },
  { id: 24, name: 'Alaba',           role: 'DC',  number: 4,  birthYear: 1992, nationality: 'Austria' },
  { id: 25, name: 'Theo Hernandez',  role: 'TS',  number: 19, birthYear: 1997, nationality: 'Francia' },
  { id: 26, name: 'Pedri',           role: 'CC',  number: 8,  birthYear: 2002, nationality: 'Spagna' },
  { id: 27, name: 'Gavi',            role: 'CC',  number: 6,  birthYear: 2004, nationality: 'Spagna' },
  { id: 28, name: 'Bellingham',      role: 'TRQ', number: 5,  birthYear: 2003, nationality: 'Inghilterra' },
  { id: 29, name: 'Vinicius Jr',     role: 'ALS', number: 7,  birthYear: 2000, nationality: 'Brasile' },
  { id: 30, name: 'Rodrygo',         role: 'ALD', number: 11, birthYear: 2001, nationality: 'Brasile' },
  { id: 31, name: 'Mbappe',          role: 'ATT', number: 9,  birthYear: 1998, nationality: 'Francia' },
  // 🇫🇷 Francesi / Inglesi
  { id: 32, name: 'Maignan',         role: 'POR', number: 1,  birthYear: 1995, nationality: 'Francia' },
  { id: 33, name: 'Hernandez T.',    role: 'DC',  number: 23, birthYear: 1999, nationality: 'Francia' },
  { id: 34, name: 'Tchouameni',      role: 'CDC', number: 8,  birthYear: 2000, nationality: 'Francia' },
  { id: 35, name: 'Camavinga',       role: 'CC',  number: 12, birthYear: 2002, nationality: 'Francia' },
  { id: 36, name: 'Salah',           role: 'ALD', number: 11, birthYear: 1992, nationality: 'Egitto' },
  { id: 37, name: 'De Bruyne',       role: 'TRQ', number: 17, birthYear: 1991, nationality: 'Belgio' },
  { id: 38, name: 'Haaland',         role: 'ATT', number: 9,  birthYear: 2000, nationality: 'Norvegia' },
  { id: 39, name: 'Kane',            role: 'ATT', number: 9,  birthYear: 1993, nationality: 'Inghilterra' },
  { id: 40, name: 'Son',             role: 'ALS', number: 7,  birthYear: 1992, nationality: 'Corea del Sud' },
  { id: 41, name: 'Saka',            role: 'ALD', number: 7,  birthYear: 2001, nationality: 'Inghilterra' },
  { id: 42, name: 'Odegaard',        role: 'TRQ', number: 8,  birthYear: 1998, nationality: 'Norvegia' },
  { id: 43, name: 'Ruben Dias',      role: 'DC',  number: 3,  birthYear: 1997, nationality: 'Portogallo' },
  { id: 44, name: 'Cancelo',         role: 'TD',  number: 27, birthYear: 1994, nationality: 'Portogallo' },
  { id: 45, name: 'Bruno Fernandes', role: 'TRQ', number: 8,  birthYear: 1994, nationality: 'Portogallo' },
  { id: 46, name: 'Wirtz',           role: 'TRQ', number: 10, birthYear: 2003, nationality: 'Germania' },
  { id: 47, name: 'Musiala',         role: 'CC',  number: 10, birthYear: 2003, nationality: 'Germania' },
  { id: 48, name: 'Rudiger',         role: 'DC',  number: 22, birthYear: 1993, nationality: 'Germania' },
])

// ── Carica teams all'avvio ─────────────────────────────
onMounted(() => loadTeams())

// ── Computed ────────────────────────────────────────────
const currentPositions = computed(() => FORMATIONS[formation.value]?.positions || [])

const filledCount = computed(() =>
  currentPositions.value.filter(p => getPlayer(p.id, 0)?.trim()).length
)

// ── Helpers player slots ────────────────────────────────
const getPlayer = (posId, slot) => players[posId]?.[slot] || ''

const setPlayer = (posId, slot, name) => {
  // Con reactive() la mutazione diretta è sempre tracciata da Vue 3
  if (!players[posId]) {
    players[posId] = ['', '', '']
  }
  players[posId][slot] = name
}

const clearPosition = (posId) => {
  players[posId] = ['', '', '']
}

// ── Helpers UI ──────────────────────────────────────────
const roleColor = (label) => ROLE_COLORS[label] || '#6b7280'

const formatDate = (dt) => new Date(dt).toLocaleDateString('it-IT', {
  day: '2-digit', month: '2-digit', year: 'numeric',
  hour: '2-digit', minute: '2-digit',
})

const notify = (msg, type = 'success') => {
  notification.value = { msg, type }
  setTimeout(() => { notification.value = null }, 2800)
}

// ── Azioni ──────────────────────────────────────────────
const selectPosition = (pos) => { selectedPos.value = pos }

const changeFormation = (f) => {
  formation.value = f
  Object.keys(players).forEach(k => delete players[k])
  selectedPos.value = null
}

const resetForm = () => {
  teamId.value = null
  teamName.value = ''
  formation.value = '4-3-3'
  // svuota reactive: elimina tutte le chiavi
  Object.keys(players).forEach(k => delete players[k])
  selectedPos.value = null
}

// ── Anagrafica ──────────────────────────────────────────
const onAddNew = (name, slotIndex) => {
  addingNew.value = {
    name,
    posId: selectedPos.value?.id,
    slotIndex,
    posLabel: selectedPos.value?.label,
  }
}

const onConfirmAddNew = ({ role, number, birthYear, nationality }) => {
  const newPlayer = { id: Date.now(), name: addingNew.value.name, role, number, birthYear, nationality }
  registry.value.push(newPlayer)
  if (addingNew.value.posId !== undefined) {
    setPlayer(addingNew.value.posId, addingNew.value.slotIndex, addingNew.value.name)
  }
  addingNew.value = null
  notify(`✅ "${newPlayer.name}" aggiunto all'anagrafica`)
}

const onRegistrySave = (updated) => {
  registry.value = updated
  showRegistry.value = false
  notify('Anagrafica salvata')
}

// ── API Squadre ─────────────────────────────────────────
const loadTeams = async () => {
  loading.value = true
  try {
    const res = await teamsApi.getAll()
    savedTeams.value = res.data
  } catch { notify('Errore nel caricamento', 'error') }
  finally { loading.value = false }
}

const loadTeam = async (id) => {
  try {
    const res = await teamsApi.getById(id)
    const team = res.data
    teamId.value   = team.id
    teamName.value = team.name
    formation.value = team.formation
    // Ricostruisci players come array per slot
    const p = {}
    team.players.forEach(pl => {
      if (!p[pl.position_id]) p[pl.position_id] = ['', '', '']
      const slot = pl.slot ?? 0
      p[pl.position_id][slot] = pl.name
    })
    // Svuota e ricarica il reactive
    Object.keys(players).forEach(k => delete players[k])
    Object.assign(players, p)
    selectedPos.value = null
    tab.value = 'editor'
    notify(`📂 "${team.name}" caricata`)
  } catch { notify('Errore nel caricamento della squadra', 'error') }
}

const saveTeam = async () => {
  if (!teamName.value.trim()) { notify('Inserisci il nome della squadra!', 'error'); return }
  if (filledCount.value < 11) { notify(`Completa i titolari (${filledCount.value}/11)`, 'error'); return }
  saving.value = true
  try {
    // Serializza players array in lista piatta con slot 0/1/2
    const playersList = []
    currentPositions.value.forEach(pos => {
      const arr = players[pos.id] || ['', '', '']   // reactive, no .value
      arr.forEach((name, slot) => {
        if (name?.trim()) {
          playersList.push({
            position_id:    pos.id,
            position_label: pos.label,
            name:           name.trim(),
            slot,
          })
        }
      })
    })
    console.log('📤 Payload players:', JSON.stringify(playersList, null, 2))
    const payload = { name: teamName.value.trim(), formation: formation.value, players: playersList }
    if (teamId.value) {
      await teamsApi.update(teamId.value, payload)
    } else {
      const res = await teamsApi.create(payload)
      teamId.value = res.data.id
    }
    notify(`✅ "${teamName.value}" salvata!`)
  } catch (e) {
    console.error('❌ Errore salvataggio:', e)
    console.error('Response:', e.response?.data)
    const msg = e.response?.data?.detail || e.message || 'Errore nel salvataggio'
    notify(msg, 'error')
  } finally { saving.value = false }
}

const handleExportWord = async () => {
  if (!teamName.value.trim()) { notify('Inserisci il nome della squadra prima di esportare!', 'error'); return }
  exporting.value = true
  try {
    // il campo viene ridisegnato direttamente su canvas nell'export
    await exportToWord({
      teamName: teamName.value,
      formation: formation.value,
      players: players,
      positions: currentPositions.value,
      registry: registry.value,
    })
    notify('✅ File Word generato!')
  } catch (e) {
    console.error(e)
    notify('Errore nella generazione del Word', 'error')
  } finally {
    exporting.value = false
  }
}

const deleteTeam = async (id) => {
  if (!confirm('Eliminare questa squadra?')) return
  try {
    await teamsApi.delete(id)
    savedTeams.value = savedTeams.value.filter(t => t.id !== id)
    notify('Squadra eliminata')
  } catch { notify("Errore nell'eliminazione", 'error') }
}
</script>

<style scoped>
.editor { max-width: 1100px; margin: 0 auto; padding: 16px; font-family: 'Inter', sans-serif; color: white; }

.header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; }
.header h1 { margin: 0; font-size: 20px; color: #22c55e; }
.btn-registry {
  background: #1e293b; border: 1px solid #334155; border-radius: 8px;
  padding: 7px 14px; color: #94a3b8; cursor: pointer; font-size: 12px; font-weight: 600;
}

.tabs { display: flex; gap: 8px; margin-bottom: 16px; }
.tabs button { flex: 1; padding: 10px; border: none; border-radius: 8px; cursor: pointer; font-weight: 600; font-size: 13px; background: #1e293b; color: #94a3b8; }
.tabs button.active { background: #22c55e; color: white; }

.notification { position: fixed; top: 16px; left: 50%; transform: translateX(-50%); padding: 10px 20px; border-radius: 8px; font-weight: 600; font-size: 14px; z-index: 1000; box-shadow: 0 4px 12px rgba(0,0,0,0.3); }
.notification.success { background: #22c55e; color: white; }
.notification.error   { background: #ef4444; color: white; }
.fade-enter-active, .fade-leave-active { transition: opacity 0.3s; }
.fade-enter-from, .fade-leave-to { opacity: 0; }

.editor-layout { display: grid; grid-template-columns: 1.4fr 1fr; gap: 16px; align-items: start; }
@media (max-width: 720px) { .editor-layout { grid-template-columns: 1fr; } }

.pitch-col, .roster-col { display: flex; flex-direction: column; gap: 12px; }

.field-group label { display: block; font-size: 11px; color: #64748b; margin-bottom: 4px; text-transform: uppercase; }
.text-input { width: 100%; background: #1e293b; border: 1px solid #334155; border-radius: 8px; padding: 10px 14px; color: white; font-size: 14px; outline: none; box-sizing: border-box; }
.formation-pills { display: flex; flex-wrap: wrap; gap: 6px; }
.formation-pills button { padding: 5px 12px; border-radius: 20px; border: none; cursor: pointer; font-weight: 700; font-size: 12px; background: #1e293b; color: #94a3b8; }
.formation-pills button.active { background: #22c55e; color: white; }

.player-input-box { background: #1e293b; border-radius: 10px; padding: 14px; border: 1px solid #334155; display: flex; flex-direction: column; gap: 10px; }
.role-header { display: flex; align-items: center; gap: 10px; }
.role-badge { display: inline-block; padding: 3px 12px; border-radius: 20px; color: white; font-size: 11px; font-weight: 700; }
.role-label-text { font-size: 13px; color: #94a3b8; }
.slot-row { display: flex; flex-direction: column; gap: 4px; }
.slot-label { font-size: 10px; color: #64748b; text-transform: uppercase; font-weight: 600; }

.player-input-placeholder { background: #1e293b; border: 1px dashed #334155; border-radius: 10px; padding: 24px; text-align: center; color: #475569; font-size: 12px; }

.roster-list { background: #1e293b; border-radius: 10px; padding: 10px; border: 1px solid #334155; max-height: 360px; overflow-y: auto; }
.roster-header { font-size: 11px; color: #64748b; margin-bottom: 8px; }
.progress-bar { height: 3px; background: #334155; border-radius: 2px; margin-top: 4px; }
.progress-fill { height: 100%; background: #22c55e; border-radius: 2px; transition: width 0.3s; }

.roster-item { display: flex; align-items: center; gap: 8px; padding: 6px 8px; border-radius: 6px; cursor: pointer; margin-bottom: 2px; }
.roster-item:hover, .roster-item.selected { background: #0f172a; }
.role-tag { font-size: 10px; font-weight: 700; width: 30px; text-align: center; background: rgba(255,255,255,0.07); border-radius: 4px; padding: 1px 3px; flex-shrink: 0; }
.roster-names { display: flex; flex-direction: column; gap: 1px; flex: 1; min-width: 0; }
.roster-name-starter { font-size: 12px; color: white; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.roster-name-reserve { font-size: 10px; color: #64748b; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.roster-item:not(.filled) .roster-name-starter { color: #475569; }
.clear-btn { background: none; border: none; color: #475569; cursor: pointer; font-size: 14px; padding: 0 2px; flex-shrink: 0; }
.clear-btn:hover { color: #ef4444; }

.actions { display: flex; gap: 8px; }
.btn-primary { flex: 1; background: #22c55e; border: none; border-radius: 8px; padding: 12px; color: white; font-weight: 700; font-size: 14px; cursor: pointer; }
.btn-primary:disabled { opacity: 0.6; cursor: not-allowed; }
.btn-secondary { background: #1e293b; border: none; border-radius: 8px; padding: 12px 16px; color: #94a3b8; cursor: pointer; font-size: 14px; }

.teams-tab { display: flex; flex-direction: column; gap: 10px; }
.empty-state { background: #1e293b; border-radius: 12px; padding: 40px; text-align: center; color: #475569; }
.empty-icon { font-size: 40px; margin-bottom: 8px; }
.empty-sub { font-size: 12px; margin-top: 4px; }
.team-cards { display: flex; flex-direction: column; gap: 10px; }
.team-card { background: #1e293b; border-radius: 12px; padding: 14px; border: 1px solid #334155; }
.team-card-header { display: flex; justify-content: space-between; align-items: center; }
.team-card-name { font-weight: 700; font-size: 15px; }
.team-card-meta { font-size: 12px; color: #64748b; margin-top: 2px; }
.team-card-meta strong { color: #22c55e; }
.team-card-actions { display: flex; gap: 6px; }
.btn-load { background: #22c55e; border: none; border-radius: 6px; padding: 6px 14px; color: white; cursor: pointer; font-size: 12px; font-weight: 600; }
.btn-delete { background: #450a0a; border: none; border-radius: 6px; padding: 6px 10px; color: #ef4444; cursor: pointer; font-size: 12px; }
.btn-export { width: 100%; background: #1e3a5f; border: 1px solid #2563eb; border-radius: 8px; padding: 11px; color: #93c5fd; font-weight: 600; font-size: 13px; cursor: pointer; margin-top: 2px; }
.btn-export:hover { background: #1e40af; color: white; }
.btn-export:disabled { opacity: 0.6; cursor: not-allowed; }
</style>