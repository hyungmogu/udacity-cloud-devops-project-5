import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueJsx from '@vitejs/plugin-vue-jsx'
import dotenv from 'dotenv'

dotenv.config({
  path: fileURLToPath(new URL('./.env', import.meta.url))
})

// https://vitejs.dev/config/
export default defineConfig({
  base: process.env.IS_PRODUCTION === "true" ? "/" : "/udacity-cloud-devops-project-5/preview/",
  plugins: [vue(), vueJsx()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})
