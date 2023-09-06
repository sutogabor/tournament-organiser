import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/tournament': 'http://localhost:8080',
      '/player': 'http://localhost:8080',
      '/matches': 'http://localhost:8080',
    },
  },
})
