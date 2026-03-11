<script setup lang="ts">

import {useRoute} from "vue-router";

const route = useRoute()

</script>

<template>
  用户空间：{{ route.params.user_id}}
</template>

<style scoped>

</style>
