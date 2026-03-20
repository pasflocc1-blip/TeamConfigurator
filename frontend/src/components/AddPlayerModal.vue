<template>
  <div class="modal-overlay">
    <div class="modal">
      <h3 class="modal-title">➕ Aggiungi "{{ name }}"</h3>
      <div class="modal-body">
        <div class="field">
          <label>RUOLO</label>
          <select v-model="role" class="form-select">
            <option v-for="r in ALL_ROLES" :key="r" :value="r">{{ r }}</option>
          </select>
        </div>
        <div class="field-row">
          <div class="field">
            <label>NUMERO MAGLIA</label>
            <input v-model="number" type="number" placeholder="Es: 10" class="form-input" />
          </div>
          <div class="field">
            <label>ANNO DI NASCITA</label>
            <input v-model="birthYear" type="number" placeholder="Es: 1999" min="1960" max="2010" class="form-input" />
          </div>
        </div>
        <div class="field">
          <label>NAZIONALITÀ <span style="color:#475569">(opzionale)</span></label>
          <input v-model="nationality" placeholder="Es: Italia, Francia..." class="form-input" />
        </div>
        <div class="modal-actions">
          <button @click="$emit('cancel')" class="btn-cancel">Annulla</button>
          <button @click="confirm" class="btn-confirm">✓ Conferma</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { ALL_ROLES } from '@/composables/useFormations'

const props = defineProps({ name: String, posLabel: String })
const emit  = defineEmits(['cancel', 'confirm'])

const role        = ref(props.posLabel || 'ATT')
const number      = ref('')
const birthYear   = ref('')
const nationality = ref('')

const confirm = () => emit('confirm', {
  role: role.value,
  number: number.value ? parseInt(number.value) : null,
  birthYear: birthYear.value ? parseInt(birthYear.value) : null,
  nationality: nationality.value.trim() || null,
})
</script>

<style scoped>
.modal-overlay {
  position: fixed; inset: 0; background: rgba(0,0,0,0.78); z-index: 210;
  display: flex; align-items: center; justify-content: center; padding: 16px;
}
.modal {
  background: #1e293b; border: 1px solid #334155; border-radius: 16px;
  padding: 24px; width: 100%; max-width: 360px;
}
.modal-title { margin: 0 0 18px; color: white; font-size: 15px; }
.modal-body  { display: flex; flex-direction: column; gap: 12px; }
.field       { display: flex; flex-direction: column; gap: 4px; }
.field-row   { display: flex; gap: 10px; }
.field-row .field { flex: 1; }
.field label { font-size: 10px; color: #64748b; text-transform: uppercase; font-weight: 600; }
.form-select, .form-input {
  background: #0f172a; border: 1px solid #334155; border-radius: 8px;
  padding: 9px 10px; color: white; font-size: 14px; outline: none;
  width: 100%; box-sizing: border-box;
}
.modal-actions { display: flex; gap: 8px; margin-top: 4px; }
.btn-cancel {
  flex: 1; background: #334155; border: none; border-radius: 8px;
  padding: 11px; color: #94a3b8; cursor: pointer; font-size: 13px;
}
.btn-confirm {
  flex: 1; background: #22c55e; border: none; border-radius: 8px;
  padding: 11px; color: white; font-weight: 700; cursor: pointer; font-size: 13px;
}
</style>