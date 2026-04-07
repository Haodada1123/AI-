<script setup>
import SendIcon from "@/components/character/icons/SendIcon.vue";
import MicIcon from "@/components/character/icons/MicIcon.vue";
import {ref, useTemplateRef} from "vue";
import streamApi from "@/js/http/streamApi.js";
import Microphone from "@/components/character/chat_field/input_field/Microphone.vue";

const inputRef = useTemplateRef('input-ref')
const message = ref('') //响应式变量：值变了，页面自动更新。v-model 是双向绑定，把输入框的值和响应式变量绑定在一起，任何一方变化都会同步到另一方。
const props = defineProps(['friendId'])
const emit = defineEmits(['pushBackMessage','addToLastMessage'])

const showMic = ref(false)
let processId = 0

function focus() {
  inputRef.value.focus()
}

async function handleSend(event, audio_msg) {
  let content
  if (audio_msg){
    content = audio_msg.trim()
  }else{
    const content = message.value.trim()
  }
  if (!content) return

  const curId = ++ processId

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
         if (curId !== processId) return

         if (data.content) {
          emit('addToLastMessage', data.content)
        }
      },
      onerror(err) {
      },
    })
  } catch (err){
  }
}

function handleStop(){
  ++ processId

}

function close(){
  ++ processId
  showMic.value =false
}

defineExpose({   //在 Vue 3 的 <script setup> 中，所有变量和方法默认是封闭的，父组件无法访问子组件内部的东西。defineExpose 就是用来主动暴露指定的内容给父组件使用。
  focus,
  close,
})

</script>

<template>
  <form v-if="!showMic" @submit.prevent="handleSend" class="absolute bottom-4 left-2 h-12 w-86 flex items-center">
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
    <div @click="showMic = true"  class="absolute right-10 w-8 h-8 flex justify-center items-center cursor-pointer">
      <MicIcon />
    </div>
  </form>
  <Microphone
      v-else
      @close="showMic = false"
      @send="handleSend"
      @send="handleStop"
  />
</template>

<style scoped>

</style>
