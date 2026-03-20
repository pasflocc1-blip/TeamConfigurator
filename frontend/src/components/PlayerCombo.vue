<template>
  <div ref="wrapper" style="position: relative">
    <div style="display:flex; gap:6px">
      <input
        v-model="query"
        @input="onInput"
        @focus="open = true"
        placeholder="Cerca o scrivi nome..."
        class="combo-input"
      />
      <button v-if="query" @mousedown.prevent="clear" class="combo-clear">×</button>
    </div>

    <div v-if="open" class="combo-dropdown">
      <!-- Risultati filtrati -->
      <div
        v-for="p in filtered"
        :key="p.id"
        @mousedown.prevent="select(p)"
        class="combo-item"
      >
        <span class="combo-role-badge" :style="{ background: roleColor(p.role) }">{{ p.role }}</span>
        <span class="combo-name">{{ p.name }}</span>
        <span v-if="p.number" class="combo-number">#{{ p.number }}</span>
      </div>

      <!-- Aggiungi nuovo -->
      <div
        v-if="query.trim() && !exactMatch"
        @mousedown.prevent="$emit('add-new', query.trim()); open = false"
        class="combo-add"
      >
        <span style="font-size:15px">＋</span>
        Aggiungi "{{ query.trim() }}" all'anagrafica
      </div>

      <div v-if="filtered.length === 0 && !query.trim()" class="combo-empty">
        Anagrafica vuota
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted, onUnmounted } from 'vue'
import { ROLE_COLORS } from '@/composables/useFormations'

// Ordine ruoli per display
const ROLE_SORT = {
  POR: 1,
  DC: 2, TD: 2, TS: 2, TLD: 2, TLS: 2,
  CDC: 3, CC: 3, CCD: 3, CCS: 3,
  TRQ: 4, ALD: 4, ALS: 4, ATT: 4,
}
const roleSort = (role) => ROLE_SORT[role] || 5

const props = defineProps({
  registry: { type: Array, default: () => [] },
  modelValue: { type: String, default: '' },
})
const emit = defineEmits(['update:modelValue', 'add-new'])

const query = ref(props.modelValue)
const open = ref(false)
const wrapper = ref(null)

watch(() => props.modelValue, v => { query.value = v })

const filtered = computed(() => {
  const list = !query.value.trim()
    ? [...props.registry]
    : props.registry.filter(p => p.name.toLowerCase().includes(query.value.toLowerCase()))
  return list.sort((a, b) => {
    const rs = roleSort(a.role) - roleSort(b.role)
    if (rs !== 0) return rs
    return a.name.localeCompare(b.name)
  })
})

const exactMatch = computed(() =>
  props.registry.some(p => p.name.toLowerCase() === query.value.trim().toLowerCase())
)

const roleColor = (r) => ROLE_COLORS[r] || '#6b7280'

const onInput = () => {
  open.value = true
  emit('update:modelValue', query.value)
}

const select = (p) => {
  query.value = p.name
  emit('update:modelValue', p.name)
  open.value = false
}

const clear = () => {
  query.value = ''
  emit('update:modelValue', '')
  open.value = true
}

const onClickOutside = (e) => {
  if (wrapper.value && !wrapper.value.contains(e.target)) open.value = false
}
onMounted(() => document.addEventListener('mousedown', onClickOutside))
onUnmounted(() => document.removeEventListener('mousedown', onClickOutside))
</script>

<style scoped>
.combo-input {
  flex: 1; background: #0f172a; border: 1px solid #334155;
  border-radius: 8px; padding: 9px 12px; color: white; font-size: 13px; outline: none; width: 100%;
}
.combo-clear {
  background: #334155; border: none; border-radius: 8px;
  padding: 0 10px; color: #94a3b8; cursor: pointer; font-size: 18px;
}
.combo-dropdown {
  position: absolute; top: calc(100% + 4px); left: 0; right: 0; z-index: 100;
  background: #1e293b; border: 1px solid #334155; border-radius: 8px;
  max-height: 200px; overflow-y: auto;
  box-shadow: 0 8px 24px rgba(0,0,0,0.5);
}
.combo-item {
  display: flex; align-items: center; gap: 10px;
  padding: 8px 12px; cursor: pointer; border-bottom: 1px solid #0f172a;
}
.combo-item:hover { background: #0f172a; }
.combo-role-badge {
  width: 26px; height: 26px; border-radius: 50%; display: flex; align-items: center;
  justify-content: center; font-size: 8px; font-weight: 700; color: white; flex-shrink: 0;
}
.combo-name { color: white; font-size: 13px; font-weight: 500; flex: 1; }
.combo-number { color: #64748b; font-size: 11px; }
.combo-meta { display: flex; gap: 6px; align-items: center; margin-left: auto; }
.combo-nat  { color: #94a3b8; font-size: 11px; }
.combo-year { color: #64748b; font-size: 11px; }
.combo-add {
  display: flex; align-items: center; gap: 8px; padding: 9px 12px;
  cursor: pointer; color: #22c55e; font-size: 13px; font-weight: 600;
  border-top: 1px solid #334155;
}
.combo-add:hover { background: #0f172a; }
.combo-empty { padding: 14px; text-align: center; color: #475569; font-size: 12px; }
</style>