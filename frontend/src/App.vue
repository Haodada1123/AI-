<script setup lang="ts">
import { onMounted } from "vue";
import NavBar from "@/components/navbar/NavBar.vue";
import { useUserStore } from "@/stores/user.js";
import api from "@/js/http/api.js";

const user = useUserStore();

onMounted(async () => {
  // 应用启动时拉取用户状态，这样导航栏才能正确显示「登录」或用户菜单
  try {
    const res = await api.get("/api/user/account/get_user_info/");
    if (res.data?.result === "success") {
      user.setUserInfo({
        user_id: res.data.user_id,
        username: res.data.username,
        photo: res.data.photo,
        profile: res.data.profile,
      });
    }
  } catch {
    // 未登录或 token 无效，保持未登录状态
  } finally {
    user.setHasPulledUserInfo(true);
  }
});
</script>

<template>
  <NavBar>
    <main class="min-h-[60vh] p-4">
      <RouterView />
    </main>
  </NavBar>
</template>

<style scoped>

</style>
