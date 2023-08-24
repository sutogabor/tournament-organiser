import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/tournament': 'http://127.0.0.1:8080',
      '/player': 'http://127.0.0.1:8080',
      '/matches': 'http://127.0.0.1:8080',
    },
  },
})
