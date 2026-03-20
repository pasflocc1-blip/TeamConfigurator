<template>
  <div class="modal-overlay" @click.self="$emit('close')">
    <div class="modal">
      <div class="modal-header">
        <span>📋 Anagrafica Calciatori ({{ localPlayers.length }})</span>
        <button @click="$emit('close')" class="modal-close">×</button>
      </div>

      <!-- Form aggiunta -->
      <div class="modal-form">
        <input v-model="newName" @keydown.enter="focusNext" ref="nameInput"
          placeholder="Nome e Cognome" class="form-input" style="flex:2 1 160px" />
        <select v-model="newRole" class="form-select">
          <option v-for="r in ALL_ROLES" :key="r" :value="r">{{ r }}</option>
        </select>
        <input v-model="newNumber" type="number" placeholder="N°" class="form-input num-input" />
        <input v-model="newYear" type="number" placeholder="Anno nascita" class="form-input year-input" min="1960" max="2010" />
        <input v-model="newNat" placeholder="🌍 Naz." class="form-input nat-input" />
        <button @click="addPlayer" class="btn-add">＋ Aggiungi</button>
      </div>

      <!-- Filtro ricerca -->
      <div class="modal-search">
        <input v-model="search" placeholder="🔍 Cerca calciatore..." class="form-input" style="width:100%" />
      </div>

      <!-- Lista -->
      <div class="modal-list">
        <div class="list-header">
          <span style="flex:2">Nome</span>
          <span style="width:42px;text-align:center">Ruolo</span>
          <span style="width:36px;text-align:center">N°</span>
          <span style="width:50px;text-align:center">Anno</span>
          <span style="width:44px;text-align:center">Naz.</span>
          <span style="width:28px"></span>
        </div>
        <div v-for="p in filteredPlayers" :key="p.id" class="registry-item">
          <span class="reg-name">{{ p.name }}</span>
          <span class="reg-role-badge" :style="{ background: roleColor(p.role) }">{{ p.role }}</span>
          <span class="reg-num">{{ p.number ?? '—' }}</span>
          <span class="reg-year">{{ p.birthYear ?? '—' }}</span>
          <span class="reg-nat">{{ p.nationality ?? '—' }}</span>
          <button @click="removePlayer(p.id)" class="reg-delete">×</button>
        </div>
        <div v-if="filteredPlayers.length === 0" class="reg-empty">Nessun calciatore trovato</div>
      </div>

      <div class="modal-footer">
        <button @click="$emit('close')" class="btn-cancel">Annulla</button>
        <button @click="$emit('save', localPlayers)" class="btn-save">💾 Salva anagrafica</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { ROLE_COLORS, ALL_ROLES } from '@/composables/useFormations'

const props = defineProps({ registry: { type: Array, default: () => [] } })
defineEmits(['close', 'save'])

const localPlayers = ref(props.registry.map(p => ({ ...p })))
const newName      = ref('')
const newRole      = ref('ATT')
const newNumber    = ref('')
const newYear      = ref('')
const newNat       = ref('')
const search       = ref('')
const nameInput    = ref(null)

const roleColor = (r) => ROLE_COLORS[r] || '#6b7280'

const filteredPlayers = computed(() =>
  !search.value.trim()
    ? localPlayers.value
    : localPlayers.value.filter(p =>
        p.name.toLowerCase().includes(search.value.toLowerCase()) ||
        p.role.toLowerCase().includes(search.value.toLowerCase()) ||
        (p.nationality || '').toLowerCase().includes(search.value.toLowerCase())
      )
)

const focusNext = () => addPlayer()

const addPlayer = () => {
  if (!newName.value.trim()) return
  localPlayers.value.push({
    id: Date.now(),
    name: newName.value.trim(),
    role: newRole.value,
    number: newNumber.value ? parseInt(newNumber.value) : null,
    birthYear: newYear.value ? parseInt(newYear.value) : null,
    nationality: newNat.value.trim() || null,
  })
  newName.value = ''; newNumber.value = ''; newYear.value = ''; newNat.value = ''
  nameInput.value?.focus()
}

const removePlayer = (id) => {
  localPlayers.value = localPlayers.value.filter(p => p.id !== id)
}
</script>

<style scoped>
.modal-overlay {
  position: fixed; inset: 0; background: rgba(0,0,0,0.78); z-index: 200;
  display: flex; align-items: center; justify-content: center; padding: 16px;
}
.modal {
  background: #0f172a; border: 1px solid #334155; border-radius: 16px;
  width: 100%; max-width: 680px; max-height: 88vh;
  display: flex; flex-direction: column; overflow: hidden;
}
.modal-header {
  display: flex; justify-content: space-between; align-items: center;
  padding: 14px 20px; border-bottom: 1px solid #1e293b;
  font-weight: 700; font-size: 15px; color: white;
}
.modal-close { background: none; border: none; color: #64748b; cursor: pointer; font-size: 22px; }
.modal-form {
  display: flex; gap: 6px; flex-wrap: wrap;
  padding: 10px 14px; border-bottom: 1px solid #1e293b;
}
.modal-search { padding: 8px 14px; border-bottom: 1px solid #1e293b; }
.form-input {
  background: #1e293b; border: 1px solid #334155; border-radius: 8px;
  padding: 7px 10px; color: white; font-size: 13px; outline: none;
}
.num-input  { width: 52px; }
.year-input { width: 100px; }
.nat-input  { width: 70px; }
.form-select {
  background: #1e293b; border: 1px solid #334155; border-radius: 8px;
  padding: 7px 8px; color: white; font-size: 13px; outline: none;
}
.btn-add {
  background: #22c55e; border: none; border-radius: 8px;
  padding: 7px 14px; color: white; font-weight: 700; cursor: pointer; font-size: 13px; white-space: nowrap;
}
.list-header {
  display: flex; align-items: center; gap: 8px;
  padding: 6px 14px; font-size: 10px; color: #64748b; text-transform: uppercase;
  border-bottom: 1px solid #1e293b; background: #0a1120;
}
.modal-list { overflow-y: auto; flex: 1; }
.registry-item {
  display: flex; align-items: center; gap: 8px;
  padding: 7px 14px; border-bottom: 1px solid #1a2535;
}
.registry-item:hover { background: #1a2535; }
.reg-name { color: white; font-size: 13px; flex: 2; }
.reg-role-badge {
  width: 42px; text-align: center; border-radius: 12px; padding: 2px 0;
  font-size: 9px; font-weight: 700; color: white; flex-shrink: 0;
}
.reg-num  { width: 36px; text-align: center; color: #64748b; font-size: 12px; }
.reg-year { width: 50px; text-align: center; color: #64748b; font-size: 12px; }
.reg-nat  { width: 44px; text-align: center; color: #94a3b8; font-size: 12px; }
.reg-delete {
  width: 28px; background: none; border: none; color: #475569;
  cursor: pointer; font-size: 17px; padding: 0; flex-shrink: 0;
}
.reg-delete:hover { color: #ef4444; }
.reg-empty { padding: 24px; text-align: center; color: #475569; font-size: 13px; }
.modal-footer {
  display: flex; justify-content: flex-end; gap: 8px;
  padding: 12px 14px; border-top: 1px solid #1e293b;
}
.btn-cancel {
  background: #1e293b; border: none; border-radius: 8px;
  padding: 10px 16px; color: #94a3b8; cursor: pointer; font-size: 13px;
}
.btn-save {
  background: #22c55e; border: none; border-radius: 8px;
  padding: 10px 16px; color: white; font-weight: 700; cursor: pointer; font-size: 13px;
}
</style>