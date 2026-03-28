<template>
  <fieldset class="fieldset">
    <label class="label text-base">名字</label>
    <input v-model="myName" type="text" class="input w-108">
  </fieldset>
</template>

<script setup lang="ts">
import {ref, watch} from "vue";

const props = defineProps(['name'])
const myName = ref(props.name)

watch(()=> props.name, newVal=>{
  myName.value = newVal
})

defineExpose({
  myName,
})

</script>

<style scoped>
</style>
