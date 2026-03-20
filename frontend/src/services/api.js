import axios from 'axios'

const api = axios.create({
  baseURL: '/api',
  headers: { 'Content-Type': 'application/json' },
})

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