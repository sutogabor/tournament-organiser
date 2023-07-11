import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/event': 'http://127.0.0.1:5000',
      '/player': 'http://127.0.0.1:5000',
      '/matches': 'http://127.0.0.1:5000',
    },
  },
})
