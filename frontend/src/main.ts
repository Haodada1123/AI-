import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import axios from 'axios' // 👈 1. 新增导入 axios (用于类型检查)

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
    // 👈 2. 使用 axios.isAxiosError 告诉 TypeScript 这是一个 Axios 错误
    if (axios.isAxiosError(error)) {
      // 现在的 error 已经是 AxiosError 类型了，可以安全地访问 .response
      if (error.response?.status === 401) {
        // 静默处理：这是正常的未登录状态
      } else {
        console.warn('加载用户信息失败:', error.message)
      }
    } else {
      // 处理非 Axios 引起的其他未知报错
      console.warn('发生了非网络请求的未知错误:', error)
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