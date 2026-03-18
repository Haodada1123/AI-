import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from '@/router/index.js'
import { useUserStore } from '@/stores/user.js'
import api from '@/js/http/api.js'

async function bootstrapAuth() {
  const user = useUserStore()
  try {
    const res = await api.get('/api/user/account/get_user_info/')
    if (res.data?.result === 'success') {
      user.setUserInfo({
        user_id: res.data.user_id,
        username: res.data.username,
        photo: res.data.photo,
        profile: res.data.profile,
      })
    }
  } catch {
    // 未登录或 refresh 失败
  } finally {
    user.setHasPulledUserInfo(true)
  }
}

const app = createApp(App)
const pinia = createPinia()
app.use(pinia)

bootstrapAuth().finally(() => {
  app.use(router)
  app.mount('#app')
})
