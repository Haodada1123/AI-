import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'homepage',
      component: () => import('@/views/homepage/HomePageIndex.vue'),
    },
    {
      path: '/friend',
      name: 'friend',
      component: () => import('@/views/friend/FriendIndex.vue'),
    },
    {
      path: '/create',
      name: 'create',
      component: () => import('@/views/create/CreateIndex.vue'),
    },
    {
      path: '/user/account/login',
      name: 'login',
      component: () => import('@/views/user/account/LoginIndex.vue'),
    },
    {
      path: '/user/account/register',
      name: 'register',
      component: () => import('@/views/user/account/RegisterIndex.vue'),
    },
    {
      path: '/user/space/:user_id',
      name: 'space',
      component: () => import('@/views/user/space/SpaceIndex.vue'),
    },
    {
      path: '/profile',
      name: 'profile',
      component: () => import('@/views/profile/ProfileIndex.vue'),
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'notFound',
      component: () => import('@/views/error/NotFoundIndex.vue'),
    },
  ],
})

export default router
