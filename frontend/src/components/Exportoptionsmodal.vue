<template>
  <div class="modal-overlay">
    <div class="modal">
      <h3 class="modal-title">📄 Esporta Formazione in Word</h3>

      <div class="options">
        <div
          class="option-card"
          :class="{ selected: choice === 'green' }"
          @click="choice = 'green'"
        >
          <div class="option-preview green-preview">
            <div class="mini-pitch green">
              <div class="mini-line h" />
              <div class="mini-circle" />
              <div class="mini-token" style="top:20%; left:45%" />
              <div class="mini-token" style="top:50%; left:20%" />
              <div class="mini-token" style="top:50%; left:45%" />
              <div class="mini-token" style="top:50%; left:70%" />
              <div class="mini-token" style="top:75%; left:45%" />
            </div>
          </div>
          <div class="option-label">🌿 Campo verde</div>
          <div class="option-desc">Sfondo verde con linee bianche</div>
        </div>

        <div
          class="option-card"
          :class="{ selected: choice === 'white' }"
          @click="choice = 'white'"
        >
          <div class="option-preview white-preview">
            <div class="mini-pitch white">
              <div class="mini-line h dark" />
              <div class="mini-circle dark" />
              <div class="mini-token dark" style="top:20%; left:45%" />
              <div class="mini-token dark" style="top:50%; left:20%" />
              <div class="mini-token dark" style="top:50%; left:45%" />
              <div class="mini-token dark" style="top:50%; left:70%" />
              <div class="mini-token dark" style="top:75%; left:45%" />
            </div>
          </div>
          <div class="option-label">🖨️ Risparmio toner</div>
          <div class="option-desc">Sfondo bianco con bordi scuri</div>
        </div>
      </div>

      <div class="modal-actions">
        <button @click="$emit('cancel')" class="btn-cancel">Annulla</button>
        <button @click="$emit('confirm', choice === 'green')" class="btn-confirm">
          📄 Esporta
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

defineEmits(['confirm', 'cancel'])
const choice = ref('green')
</script>

<style scoped>
.modal-overlay {
  position: fixed; inset: 0; background: rgba(0,0,0,0.75); z-index: 300;
  display: flex; align-items: center; justify-content: center; padding: 16px;
}
.modal {
  background: #1e293b; border: 1px solid #334155; border-radius: 16px;
  padding: 24px; width: 100%; max-width: 440px;
}
.modal-title { margin: 0 0 20px; color: white; font-size: 16px; font-weight: 700; }

.options { display: flex; gap: 12px; margin-bottom: 20px; }

.option-card {
  flex: 1; border: 2px solid #334155; border-radius: 12px;
  padding: 12px; cursor: pointer; transition: all 0.15s; text-align: center;
}
.option-card:hover { border-color: #64748b; }
.option-card.selected { border-color: #22c55e; background: rgba(34,197,94,0.08); }

.option-preview {
  border-radius: 8px; overflow: hidden; margin-bottom: 10px; height: 120px;
  display: flex; align-items: center; justify-content: center;
}
.green-preview { background: #15803d; }
.white-preview { background: white; border: 1px solid #e5e7eb; }

.mini-pitch {
  position: relative; width: 70px; height: 100px; border-radius: 3px;
}
.mini-pitch.green { border: 1.5px solid rgba(255,255,255,0.6); }
.mini-pitch.white { border: 2px solid #111; }

.mini-line { position: absolute; }
.mini-line.h { top: 50%; left: 0; right: 0; height: 1.5px; background: rgba(255,255,255,0.6); }
.mini-line.h.dark { background: #111; height: 2px; }

.mini-circle {
  position: absolute; top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  width: 22px; height: 22px; border-radius: 50%;
  border: 1.5px solid rgba(255,255,255,0.6);
}
.mini-circle.dark { border-color: #111; border-width: 2px; }

.mini-token {
  position: absolute; transform: translate(-50%, -50%);
  width: 14px; height: 10px; border-radius: 2px;
  background: white; border: 1px solid rgba(255,255,255,0.3);
  box-shadow: 0 1px 2px rgba(0,0,0,0.4);
}
.mini-token.dark { background: white; border: 1.5px solid #334155; }

.option-label { font-size: 13px; font-weight: 700; color: white; margin-bottom: 4px; }
.option-desc { font-size: 11px; color: #64748b; }

.modal-actions { display: flex; gap: 8px; }
.btn-cancel {
  flex: 1; background: #334155; border: none; border-radius: 8px;
  padding: 11px; color: #94a3b8; cursor: pointer; font-size: 13px;
}
.btn-confirm {
  flex: 2; background: #22c55e; border: none; border-radius: 8px;
  padding: 11px; color: white; font-weight: 700; cursor: pointer; font-size: 14px;
}
</style>
