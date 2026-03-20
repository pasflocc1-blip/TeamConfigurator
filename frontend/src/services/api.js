import axios from 'axios'

// In sviluppo: Vite proxy manda /api → localhost:8000
// In produzione (PyInstaller Mac): FastAPI serve tutto su localhost:8000
// baseURL = '/api' funziona in entrambi i casi
const api = axios.create({
  baseURL: '/api',
  headers: { 'Content-Type': 'application/json' },
  // Timeout di 10 secondi — utile su Mac dove il primo avvio può essere lento
  timeout: 10000,
})

// Interceptor: retry automatico su timeout (max 2 tentativi)
api.interceptors.response.use(
  response => response,
  async error => {
    const config = error.config
    if (!config || config.__retryCount >= 2) return Promise.reject(error)
    if (error.code === 'ECONNABORTED' || error.response?.status >= 500) {
      config.__retryCount = (config.__retryCount || 0) + 1
      await new Promise(r => setTimeout(r, 1000))
      return api(config)
    }
    return Promise.reject(error)
  }
)

// ── Squadre ──────────────────────────────────────────────
export const teamsApi = {
  getAll:   ()         => api.get('/teams'),
  getById:  (id)       => api.get(`/teams/${id}`),
  create:   (data)     => api.post('/teams', data),
  update:   (id, data) => api.put(`/teams/${id}`, data),
  delete:   (id)       => api.delete(`/teams/${id}`),
}

// ── Anagrafica ───────────────────────────────────────────
export const registryApi = {
  getAll:   (params)   => api.get('/registry', { params }),
  create:   (data)     => api.post('/registry', data),
  update:   (id, data) => api.put(`/registry/${id}`, data),
  delete:   (id)       => api.delete(`/registry/${id}`),
}

export default api