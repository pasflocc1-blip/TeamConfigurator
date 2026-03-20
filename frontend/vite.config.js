import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { resolve } from 'path'

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': resolve(__dirname, 'src'),
    },
  },
  server: {
    // Proxy per sviluppo locale: le chiamate /api vanno al backend FastAPI
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      },
    },
  },
  build: {
    // Output nella cartella backend/frontend_dist
    // così PyInstaller la trova automaticamente
    outDir: '../backend/frontend_dist',
    emptyOutDir: true,
  },
})