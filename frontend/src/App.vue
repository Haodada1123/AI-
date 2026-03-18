<script setup lang="ts">
import NavBar from "@/components/navbar/NavBar.vue";
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
