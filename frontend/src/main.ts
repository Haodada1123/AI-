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
  } catch (error) {
    // 预期的错误：用户未登录时，获取用户信息会返回 401
    // 这是正常的行为，无需处理，应用会显示登录页面
    if (error.response?.status === 401) {
      // 静默处理：这是正常的未登录状态
    } else {
      console.warn('加载用户信息失败:', error)
    }
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
