<template>
  <div class="pitch-wrapper">
    <svg ref="svgRef" viewBox="0 0 400 500" class="pitch-svg">

      <defs>
        <pattern id="stripes" patternUnits="userSpaceOnUse" width="400" height="24">
          <rect width="400" height="12" fill="#166534" />
          <rect y="12" width="400" height="12" fill="#15803d" />
        </pattern>
      </defs>
      <rect width="400" height="500" fill="url(#stripes)" rx="4" />

      <!-- Linee campo — scala 400x500 (fattore ~1.25x rispetto a 320x420) -->
      <g stroke="rgba(255,255,255,0.6)" stroke-width="0.7" fill="none">
        <!-- Bordo esterno -->
        <rect x="11" y="8" width="378" height="484" />
        <!-- Metà campo -->
        <line x1="11" y1="250" x2="389" y2="250" />
        <!-- Cerchio centrale -->
        <circle cx="200" cy="250" r="46" />
        <circle cx="200" cy="250" r="1.8" fill="rgba(255,255,255,0.6)" />
        <!-- Area grande attacco (alto) -->
        <rect x="110" y="8"  width="180" height="84" />
        <!-- Area piccola attacco -->
        <rect x="154" y="8"  width="92"  height="30" />
        <!-- Area grande difesa (basso) -->
        <rect x="110" y="408" width="180" height="84" />
        <!-- Area piccola difesa -->
        <rect x="154" y="462" width="92"  height="30" />
        <!-- Dischetti -->
        <circle cx="200" cy="60"  r="1.8" fill="rgba(255,255,255,0.6)" />
        <circle cx="200" cy="440" r="1.8" fill="rgba(255,255,255,0.6)" />
        <!-- Porte -->
        <rect x="166" y="492" width="68" height="8" />
        <rect x="166" y="0"   width="68" height="8" />
      </g>

      <!-- Token giocatori -->
      <g
        v-for="pos in positions"
        :key="pos.id"
        :transform="`translate(${pos.x}, ${pos.y})`"
        class="player-token"
        @click="$emit('select', pos)"
      >
        <!-- Glow selezione -->
        <rect v-if="isSelected(pos)"
          x="-34" y="-21" width="68" height="42"
          rx="6" fill="white" opacity="0.2"
        />

        <!-- Rettangolo bianco principale: 64x38 -->
        <rect
          x="-32" y="-19" width="64" height="38"
          rx="4"
          fill="white"
          :stroke="isSelected(pos) ? roleColor(pos.label) : 'rgba(255,255,255,0.25)'"
          :stroke-width="isSelected(pos) ? 2.5 : 0.6"
          style="filter: drop-shadow(0 2px 6px rgba(0,0,0,0.7))"
        />

        <!-- Separatore colorato -->
        <line
          x1="-32" y1="-8" x2="32" y2="-8"
          :stroke="roleColor(pos.label)"
          stroke-width="1"
        />

        <!-- Etichetta ruolo -->
        <text
          x="0" y="-12"
          text-anchor="middle"
          :fill="roleColor(pos.label)"
          font-size="6.5"
          font-weight="800"
          font-family="'Inter', Arial, sans-serif"
          letter-spacing="0.5"
        >{{ pos.label }}</text>

        <!-- Titolare -->
        <text x="0" y="-1.5"
          text-anchor="middle"
          :fill="playerNames(pos.id)[0] ? '#111827' : '#d1d5db'"
          font-size="6.2"
          font-weight="700"
          font-family="'Inter', Arial, sans-serif"
        >{{ playerNames(pos.id)[0] ? truncate(playerNames(pos.id)[0], 0) : '—' }}</text>

        <!-- Riserva 1 -->
        <text x="0" y="6"
          text-anchor="middle"
          :fill="playerNames(pos.id)[1] ? '#6b7280' : 'transparent'"
          font-size="5.5"
          font-weight="400"
          font-family="'Inter', Arial, sans-serif"
        >{{ truncate(playerNames(pos.id)[1], 1) }}</text>

        <!-- Riserva 2 -->
        <text x="0" y="13.5"
          text-anchor="middle"
          :fill="playerNames(pos.id)[2] ? '#6b7280' : 'transparent'"
          font-size="5.5"
          font-weight="400"
          font-family="'Inter', Arial, sans-serif"
        >{{ truncate(playerNames(pos.id)[2], 2) }}</text>

      </g>
    </svg>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { ROLE_COLORS } from '@/composables/useFormations'

const props = defineProps({
  positions:  { type: Array,  required: true },
  players:    { type: Object, default: () => ({}) },
  selectedId: { type: String, default: null },
  nameLimit:  { type: Number, default: 20 }
})

defineEmits(['select'])

const svgRef = ref(null)

defineExpose({
  svgRef,
  getSvg: () => svgRef.value,
})

const roleColor  = (label) => ROLE_COLORS[label] || '#4b5563'
const isSelected = (pos)   => props.selectedId === pos.id

const playerNames = (id) => {
  const arr = props.players[id]
  if (!arr) return ['', '', '']
  return [arr[0] || '', arr[1] || '', arr[2] || '']
}

const truncate = (name, slot) => {
  if (!name) return ''
  const cleanName = name.trim()
  const max = slot === 0 ? props.nameLimit : props.nameLimit - 1
  return cleanName.length > max ? cleanName.slice(0, max) + '.' : cleanName
}
</script>

<style scoped>
.pitch-wrapper { width: 100%; max-width: 100%; margin: 0 auto; }
.pitch-svg {
  width: 100%; height: auto; display: block;
  border-radius: 10px;
  box-shadow: 0 4px 28px rgba(0,0,0,0.65);
}
.player-token { cursor: pointer; }
.player-token:hover rect:nth-child(2) { opacity: 0.88; }
</style>