<template>
  <div class="modal-overlay">
    <div class="modal">
      <h3 class="modal-title">➕ Aggiungi "{{ name }}" all'anagrafica</h3>
      <div class="modal-body">
        <div class="field-row">
          <div class="field">
            <label>RUOLO</label>
            <select v-model="role" class="form-select">
              <option v-for="r in ALL_ROLES" :key="r" :value="r">{{ r }}</option>
            </select>
          </div>
          <div class="field">
            <label>NUMERO MAGLIA</label>
            <input v-model="number" type="number" placeholder="Es: 10" class="form-input" />
          </div>
        </div>
        <div class="field-row">
          <div class="field">
            <label>ANNO DI NASCITA</label>
            <input v-model="birthYear" type="number" placeholder="Es: 1994" class="form-input" />
          </div>
          <div class="field">
            <label>NAZIONALITÀ</label>
            <input v-model="nationality" placeholder="Es: Italia" class="form-input" />
          </div>
        </div>
        <div class="field">
          <label>SQUADRA</label>
          <input v-model="teamName" placeholder="Es: Juventus" class="form-input" />
        </div>
        <div v-if="error" style="color:#ef4444; font-size:12px">{{ error }}</div>
        <div class="modal-actions">
          <button @click="$emit('cancel')" class="btn-cancel">Annulla</button>
          <button @click="confirm" :disabled="saving" class="btn-confirm">
            {{ saving ? '...' : '✓ Conferma' }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { ALL_ROLES } from '@/composables/useFormations'
import { registryApi } from '@/services/api'

const props = defineProps({ name: String, posLabel: String })
const emit  = defineEmits(['cancel', 'confirm'])

const role        = ref(props.posLabel || 'ATT')
const number      = ref('')
const birthYear   = ref('')
const nationality = ref('')
const teamName    = ref('')
const saving      = ref(false)
const error       = ref('')

const confirm = async () => {
  saving.value = true
  error.value  = ''
  try {
    const res = await registryApi.create({
      name:        props.name,
      role:        role.value,
      number:      number.value   ? parseInt(number.value)   : null,
      birth_year:  birthYear.value ? parseInt(birthYear.value) : null,
      nationality: nationality.value.trim() || null,
      team_name:   teamName.value.trim()    || null,
    })
    emit('confirm', res.data)
  } catch (e) {
    error.value = 'Errore nel salvataggio'
  } finally {
    saving.value = false
  }
}
</script>

<style scoped>
.modal-overlay { position: fixed; inset: 0; background: rgba(0,0,0,0.75); z-index: 210; display: flex; align-items: center; justify-content: center; padding: 16px; }
.modal { background: #1e293b; border: 1px solid #334155; border-radius: 16px; padding: 24px; width: 100%; max-width: 380px; }
.modal-title { margin: 0 0 18px; color: white; font-size: 15px; }
.modal-body { display: flex; flex-direction: column; gap: 12px; }
.field-row { display: flex; gap: 10px; }
.field { display: flex; flex-direction: column; gap: 4px; flex: 1; }
.field label { font-size: 10px; color: #64748b; text-transform: uppercase; font-weight: 600; }
.form-select, .form-input { background: #0f172a; border: 1px solid #334155; border-radius: 8px; padding: 9px 10px; color: white; font-size: 13px; outline: none; width: 100%; box-sizing: border-box; }
.modal-actions { display: flex; gap: 8px; margin-top: 4px; }
.btn-cancel { flex: 1; background: #334155; border: none; border-radius: 8px; padding: 11px; color: #94a3b8; cursor: pointer; font-size: 13px; }
.btn-confirm { flex: 1; background: #22c55e; border: none; border-radius: 8px; padding: 11px; color: white; font-weight: 700; cursor: pointer; font-size: 13px; }
.btn-confirm:disabled { opacity: 0.6; cursor: not-allowed; }
</style>