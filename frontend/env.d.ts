/// <reference types="vite/client" />

declare module '*.vue' {
  import type { DefineComponent } from 'vue'
  const component: DefineComponent<object, object, unknown>
  export default component
}

declare module '@/stores/user.js' {
  export function useUserStore(): {
    setUserInfo: (data: Record<string, unknown>) => void
    setHasPulledUserInfo: (v: boolean) => void
  }
}

declare module '@/js/http/api.js' {
  import type { AxiosInstance } from 'axios'
  const api: AxiosInstance
  export default api
}

declare module '@/router/index.js' {
  import type { Router } from 'vue-router'
  const router: Router
  export default router
}
