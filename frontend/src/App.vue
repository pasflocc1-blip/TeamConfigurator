<template>
  <div id="app" style="background: #0f172a; min-height: 100vh;">
    <!-- Splash screen mentre il backend si avvia (solo su Mac .app) -->
    <div v-if="backendLoading" class="splash">
      <div class="splash-icon">⚽</div>
      <div class="splash-title">Football Team Builder</div>
      <div class="splash-spinner" />
      <div class="splash-msg">Avvio in corso...</div>
    </div>
    <TeamEditor v-else />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import TeamEditor from '@/views/TeamEditor.vue'
import api from '@/services/api'

const backendLoading = ref(false)

onMounted(async () => {
  // Verifica se il backend è raggiungibile
  // In sviluppo (npm run dev) è già disponibile
  // Su Mac .app potrebbe richiedere qualche secondo
  try {
    await api.get('/teams', { timeout: 500 })
  } catch (e) {
    if (e.code === 'ECONNABORTED' || e.message?.includes('Network')) {
      // Backend non ancora pronto — mostra splash e riprova
      backendLoading.value = true
      let attempts = 0
      const wait = () => setTimeout(async () => {
        attempts++
        try {
          await api.get('/teams', { timeout: 1000 })
          backendLoading.value = false
        } catch {
          if (attempts < 5) wait()
          else backendLoading.value = false // mostra l'app comunque dopo 15s
        }
      }, 1000)
      wait()
    }
    // Errore diverso (es. 404, CORS) → mostra l'app normalmente
  }
})
</script>

<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
body { background: #0f172a; font-family: 'Inter', Arial, sans-serif; }

.splash {
  display: flex; flex-direction: column; align-items: center;
  justify-content: center; min-height: 100vh; gap: 16px;
}
.splash-icon { font-size: 64px; }
.splash-title { color: #22c55e; font-size: 24px; font-weight: 700; }
.splash-spinner {
  width: 40px; height: 40px;
  border: 3px solid #334155;
  border-top-color: #22c55e;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}
.splash-msg { color: #64748b; font-size: 14px; }
@keyframes spin { to { transform: rotate(360deg); } }
</style>