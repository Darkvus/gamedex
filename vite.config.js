import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  base: '/static/',
  plugins: [vue()],
  build: {
    manifest: 'manifest.json',
    outDir: 'frontend/dist',
    rollupOptions: {
      input: 'frontend/app.js',
    },
  },
  server: {
    host: 'localhost',
    port: 5173,
  },
})
