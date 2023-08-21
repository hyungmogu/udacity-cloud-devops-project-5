import {
  fileURLToPath,
  URL
} from 'node:url'

import {
  defineConfig,
  loadEnv
} from 'vite';
import vue from '@vitejs/plugin-vue'
import vueJsx from '@vitejs/plugin-vue-jsx'

// https://vitejs.dev/config/
export default defineConfig(({
  mode
}) => {
  process.env = {
    ...process.env,
    ...loadEnv(mode, process.cwd())
  };
  return {
    base: process.env.VITE_IS_PRODUCTION === "true" ? "/" : "/udacity-cloud-devops-project-5/preview/",
    plugins: [vue(), vueJsx()],
    resolve: {
      alias: {
        '@': fileURLToPath(new URL('./src',
          import.meta.url))
      }
    }
  }
});