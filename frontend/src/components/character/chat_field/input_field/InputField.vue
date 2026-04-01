<script setup>
import SendIcon from "@/components/character/icons/SendIcon.vue";
import MicIcon from "@/components/character/icons/MicIcon.vue";
import {ref, useTemplateRef} from "vue";
import streamApi from "@/js/http/streamApi.js";

const inputRef = useTemplateRef('input-ref')
const message = ref('') //响应式变量：值变了，页面自动更新。v-model 是双向绑定，把输入框的值和响应式变量绑定在一起，任何一方变化都会同步到另一方。
const props = defineProps(['friendId'])
const emit = defineEmits(['pushBackMessage','addToLastMessage'])


let isProcessing = false

function focus() {
  inputRef.value.focus()
}

async function handleSend() {
  if (isProcessing) return
  isProcessing = true

  const content = message.value.trim()
  if (!content) return
  message.value = ''

  emit('pushBackMessage', {role : 'user', content: content, id: crypto.randomUUID()})
  emit('pushBackMessage', {role : 'ai', content: '', id : crypto.randomUUID()})

  try {
    await streamApi('/api/friend/message/chat/', {
      body: {
        friend_id: props.friendId,
        message: content,
      },
      onmessage(data,isDone) {
        if (isDone){
          isProcessing = false
        }else if (data.content) {
          emit('addToLastMessage', data.content)
        }
      },
      onerror(err){
        isProcessing = false
      },
    })
  } catch (err){
    console.log(err)
    isProcessing = false
  }
}

defineExpose({   //在 Vue 3 的 <script setup> 中，所有变量和方法默认是封闭的，父组件无法访问子组件内部的东西。defineExpose 就是用来主动暴露指定的内容给父组件使用。
  focus,
})

</script>

<template>
  <form @submit.prevent="handleSend" class="absolute bottom-4 left-2 h-12 w-86 flex items-center">
    <input
        ref="input-ref"
        v-model="message"
        class="input bg-black/30 backdrop-blur-sm text-white text-base w-full h-full rounded-2xl pr-20"
        type="text"
        placeholder="文本输入..."
    >
    <div @click="handleSend" class="absolute right-2 w-8 h-8 flex justify-center items-center cursor-pointer">
      <SendIcon />
    </div>
    <div class="absolute right-10 w-8 h-8 flex justify-center items-center cursor-pointer">
      <MicIcon />
    </div>
  </form>
</template>

<style scoped>

</style>
