<template>
  <div class="modal-overlay" @click.self="$emit('close')">
    <div class="modal">
      <div class="modal-header">
        <span>📋 Anagrafica Calciatori ({{ players.length }})</span>
        <button @click="$emit('close')" class="modal-close">×</button>
      </div>

      <!-- Form aggiunta -->
      <div class="modal-form">
        <input v-model="newName" @keydown.enter="addPlayer" ref="inputName"
          placeholder="Nome e Cognome" class="form-input" style="flex:2 1 160px" />
        <select v-model="newRole" class="form-select">
          <option v-for="r in ALL_ROLES" :key="r" :value="r">{{ r }}</option>
        </select>
        <input v-model="newNumber" type="number" placeholder="Maglia"
          class="form-input" style="width:68px" />
        <input v-model="newYear" type="number" placeholder="Anno"
          class="form-input" style="width:72px" />
        <input v-model="newNationality" placeholder="Nazione"
          class="form-input" style="width:90px" />
        <input v-model="newTeamName" placeholder="Squadra"
          class="form-input" style="width:100px" />
        <button @click="addPlayer" :disabled="saving" class="btn-add">＋</button>
      </div>

      <!-- Filtri ricerca -->
      <div class="modal-filters">
        <input v-model="search" placeholder="🔍 Cerca nome..."
          class="form-input" style="flex:1" />
        <select v-model="filterRole" class="form-select">
          <option value="">Tutti i ruoli</option>
          <option v-for="r in ALL_ROLES" :key="r" :value="r">{{ r }}</option>
        </select>
        <select v-model="filterTeam" class="form-select">
          <option value="">Tutte le squadre</option>
          <option v-for="t in teamList" :key="t" :value="t">{{ t }}</option>
        </select>
      </div>

      <!-- Loading -->
      <div v-if="loading" class="reg-empty">⏳ Caricamento...</div>

      <!-- Lista -->
      <div v-else class="modal-list">
        <div v-for="p in filteredPlayers" :key="p.id" class="registry-item">
          <span class="reg-role-badge" :style="{ background: roleColor(p.role) }">{{ p.role }}</span>
          <div class="reg-info">
            <span class="reg-name">{{ p.name }}</span>
            <span class="reg-meta">
              <span v-if="p.team_name" class="reg-team">{{ p.team_name }}</span>
              <span v-if="p.nationality" class="reg-flag">{{ p.nationality }}</span>
              <span v-if="p.birth_year" class="reg-year">{{ p.birth_year }}</span>
              <span v-if="p.number" class="reg-num">#{{ p.number }}</span>
            </span>
          </div>
          <button @click="removePlayer(p.id)" class="reg-delete">×</button>
        </div>
        <div v-if="filteredPlayers.length === 0" class="reg-empty">
          Nessun calciatore trovato
        </div>
      </div>

      <div class="modal-footer">
        <span class="reg-count">{{ filteredPlayers.length }} / {{ players.length }} calciatori</span>
        <button @click="$emit('close')" class="btn-cancel">Chiudi</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { ROLE_COLORS, ALL_ROLES } from '@/composables/useFormations'
import { registryApi } from '@/services/api'

const emit = defineEmits(['close', 'updated'])

const players        = ref([])
const loading        = ref(true)
const saving         = ref(false)
const search         = ref('')
const filterRole     = ref('')
const filterTeam     = ref('')
const newName        = ref('')
const newRole        = ref('ATT')
const newNumber      = ref('')
const newYear        = ref('')
const newNationality = ref('')
const newTeamName    = ref('')
const inputName      = ref(null)

const roleColor = (r) => ROLE_COLORS[r] || '#6b7280'

const teamList = computed(() =>
  [...new Set(players.value.map(p => p.team_name).filter(Boolean))].sort()
)

const filteredPlayers = computed(() =>
  players.value.filter(p => {
    const matchSearch = !search.value ||
      p.name.toLowerCase().includes(search.value.toLowerCase())
    const matchRole = !filterRole.value || p.role === filterRole.value
    const matchTeam = !filterTeam.value || p.team_name === filterTeam.value
    return matchSearch && matchRole && matchTeam
  })
)

const loadPlayers = async () => {
  loading.value = true
  try {
    const res = await registryApi.getAll()
    players.value = res.data
  } catch (e) {
    console.error('Errore caricamento anagrafica:', e)
  } finally {
    loading.value = false
  }
}

const addPlayer = async () => {
  if (!newName.value.trim()) return
  saving.value = true
  try {
    await registryApi.create({
      name:        newName.value.trim(),
      role:        newRole.value,
      number:      newNumber.value    ? parseInt(newNumber.value)  : null,
      birth_year:  newYear.value      ? parseInt(newYear.value)    : null,
      nationality: newNationality.value.trim() || null,
      team_name:   newTeamName.value.trim()    || null,
    })
    newName.value = ''
    newNumber.value = ''
    newYear.value = ''
    newNationality.value = ''
    newTeamName.value = ''
    await loadPlayers()
    emit('updated')
    inputName.value?.focus()
  } catch (e) {
    console.error('Errore aggiunta:', e)
  } finally {
    saving.value = false
  }
}

const removePlayer = async (id) => {
  try {
    await registryApi.delete(id)
    players.value = players.value.filter(p => p.id !== id)
    emit('updated')
  } catch (e) {
    console.error('Errore eliminazione:', e)
  }
}

onMounted(loadPlayers)
</script>

<style scoped>
.modal-overlay { position: fixed; inset: 0; background: rgba(0,0,0,0.75); z-index: 200; display: flex; align-items: center; justify-content: center; padding: 16px; }
.modal { background: #0f172a; border: 1px solid #334155; border-radius: 16px; width: 100%; max-width: 660px; max-height: 88vh; display: flex; flex-direction: column; overflow: hidden; }
.modal-header { display: flex; justify-content: space-between; align-items: center; padding: 16px 20px; border-bottom: 1px solid #1e293b; font-weight: 700; font-size: 15px; color: white; }
.modal-close { background: none; border: none; color: #64748b; cursor: pointer; font-size: 22px; }
.modal-form { display: flex; gap: 6px; flex-wrap: wrap; padding: 10px 14px; border-bottom: 1px solid #1e293b; align-items: center; }
.modal-filters { display: flex; gap: 6px; padding: 8px 14px; border-bottom: 1px solid #1e293b; }
.form-input { background: #1e293b; border: 1px solid #334155; border-radius: 8px; padding: 7px 10px; color: white; font-size: 13px; outline: none; }
.form-select { background: #1e293b; border: 1px solid #334155; border-radius: 8px; padding: 7px 8px; color: white; font-size: 13px; outline: none; }
.btn-add { background: #22c55e; border: none; border-radius: 8px; padding: 7px 14px; color: white; font-weight: 700; cursor: pointer; font-size: 14px; }
.btn-add:disabled { opacity: 0.6; cursor: not-allowed; }
.modal-list { overflow-y: auto; flex: 1; }
.registry-item { display: flex; align-items: center; gap: 10px; padding: 8px 14px; border-bottom: 1px solid #1e293b; }
.reg-role-badge { width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 8px; font-weight: 700; color: white; flex-shrink: 0; }
.reg-info { flex: 1; min-width: 0; }
.reg-name { color: white; font-size: 13px; font-weight: 600; display: block; }
.reg-meta { display: flex; gap: 8px; margin-top: 2px; flex-wrap: wrap; }
.reg-team { color: #22c55e; font-size: 11px; font-weight: 600; }
.reg-flag { color: #94a3b8; font-size: 11px; }
.reg-year { color: #64748b; font-size: 11px; }
.reg-num { color: #64748b; font-size: 11px; }
.reg-delete { background: none; border: none; color: #475569; cursor: pointer; font-size: 18px; padding: 0 4px; }
.reg-delete:hover { color: #ef4444; }
.reg-empty { padding: 24px; text-align: center; color: #475569; font-size: 13px; }
.modal-footer { display: flex; justify-content: flex-end; align-items: center; gap: 8px; padding: 12px 14px; border-top: 1px solid #1e293b; }
.reg-count { color: #64748b; font-size: 12px; margin-right: auto; }
.btn-cancel { background: #1e293b; border: none; border-radius: 8px; padding: 10px 16px; color: #94a3b8; cursor: pointer; font-size: 13px; }
</style>