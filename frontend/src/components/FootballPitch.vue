<template>
  <div class="pitch-wrapper">
    <svg ref="svgRef" viewBox="0 0 320 420" class="pitch-svg">

      <defs>
        <pattern id="stripes" patternUnits="userSpaceOnUse" width="320" height="24">
          <rect width="320" height="12" fill="#166534" />
          <rect y="12" width="320" height="12" fill="#15803d" />
        </pattern>
      </defs>
      <rect width="320" height="420" fill="url(#stripes)" rx="4" />

      <!-- Linee campo -->
      <g stroke="rgba(255,255,255,0.6)" stroke-width="0.6" fill="none">
        <rect x="9" y="7" width="302" height="406" />
        <line x1="9" y1="210" x2="311" y2="210" />
        <circle cx="160" cy="210" r="37" />
        <circle cx="160" cy="210" r="1.5" fill="rgba(255,255,255,0.6)" />
        <rect x="88" y="7"   width="144" height="70" />
        <rect x="123" y="7" width="74"  height="25" />
        <rect x="88" y="343"  width="144" height="70" />
        <rect x="123" y="388" width="74"  height="25" />
        <circle cx="160" cy="50"  r="1.5" fill="rgba(255,255,255,0.6)" />
        <circle cx="160" cy="370" r="1.5" fill="rgba(255,255,255,0.6)" />
        <rect x="133" y="413" width="54" height="7" />
        <rect x="133" y="0"   width="54" height="7" />
      </g>

      <!-- Token giocatori — rettangoli più grandi: 52x34 -->
      <g
        v-for="pos in positions"
        :key="pos.id"
        :transform="`translate(${pos.x}, ${pos.y})`"
        class="player-token"
        @click="$emit('select', pos)"
      >
        <!-- Glow selezione -->
        <rect
          v-if="isSelected(pos)"
          x="-28" y="-19" width="56" height="38"
          rx="5" fill="white" opacity="0.2"
        />

        <!-- Rettangolo bianco principale -->
        <rect
          x="-26" y="-17" width="52" height="34"
          rx="4"
          fill="white"
          :stroke="isSelected(pos) ? roleColor(pos.label) : 'rgba(255,255,255,0.2)'"
          :stroke-width="isSelected(pos) ? 2.5 : 0.6"
          style="filter: drop-shadow(0 2px 6px rgba(0,0,0,0.7))"
        />

        <!-- Separatore colorato ruolo/nomi -->
        <line
          x1="-26" y1="-7" x2="26" y2="-7"
          :stroke="roleColor(pos.label)"
          stroke-width="1"
        />

        <!-- Etichetta ruolo -->
        <text
          x="0" y="-10.5"
          text-anchor="middle"
          :fill="roleColor(pos.label)"
          font-size="5.5"
          font-weight="800"
          font-family="'Inter', Arial, sans-serif"
          letter-spacing="0.4"
        >{{ pos.label }}</text>

        <!-- Titolare -->
        <text
          x="0" y="-1"
          text-anchor="middle"
          :fill="playerNames(pos.id)[0] ? '#111827' : '#d1d5db'"
          font-size="5.2"
          font-weight="700"
          font-family="'Inter', Arial, sans-serif"
        >{{ playerNames(pos.id)[0] ? truncate(playerNames(pos.id)[0], 0) : '—' }}</text>

        <!-- Riserva 1 -->
        <text
          x="0" y="5.5"
          text-anchor="middle"
          :fill="playerNames(pos.id)[1] ? '#6b7280' : 'transparent'"
          font-size="4.6"
          font-weight="600"
          font-family="'Inter', Arial, sans-serif"
        >{{ truncate(playerNames(pos.id)[1], 1) }}</text>

        <!-- Riserva 2 -->
        <text
          x="0" y="12"
          text-anchor="middle"
          :fill="playerNames(pos.id)[2] ? '#9ca3af' : 'transparent'"
          font-size="4.2"
          font-weight="500"
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
})

defineEmits(['select'])

const svgRef = ref(null)
defineExpose({ svgRef })

const roleColor  = (label) => ROLE_COLORS[label] || '#4b5563'
const isSelected = (pos)   => props.selectedId === pos.id

const playerNames = (id) => {
  const arr = props.players[id]
  if (!arr) return ['', '', '']
  return [arr[0] || '', arr[1] || '', arr[2] || '']
}

const truncate = (name, slot) => {
  if (!name) return ''
  const surname = name.trim().split(' ').pop()
  const max = slot === 0 ? 10 : 9
  return surname.length > max ? surname.slice(0, max) + '.' : surname
}
</script>

<style scoped>
.pitch-wrapper { width: 100%; max-width: 100%; margin: 0 auto; }
.pitch-svg {
  width: 100%; height: auto; display: block;
  border-radius: 10px; box-shadow: 0 4px 28px rgba(0,0,0,0.65);
}
.player-token { cursor: pointer; }
.player-token:hover rect:nth-child(2) { opacity: 0.88; }
</style>