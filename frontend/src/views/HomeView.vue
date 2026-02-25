<script setup>
import { onMounted, ref } from 'vue'
import { createTask, fetchTasks } from '../services/api'

const tasks = ref([])
const title = ref('')

async function loadTasks() {
  tasks.value = await fetchTasks()
}

async function addTask() {
  if (!title.value.trim()) return
  const task = await createTask(title.value)
  tasks.value.push(task)
  title.value = ''
}

onMounted(loadTasks)
</script>

<template>
  <section class="panel">
    <h2>Tasks</h2>
    <div class="form-row">
      <input v-model="title" placeholder="输入任务标题" @keyup.enter="addTask" />
      <button @click="addTask">添加</button>
    </div>
    <ul>
      <li v-for="task in tasks" :key="task.id">{{ task.title }}</li>
    </ul>
  </section>
</template>

<style scoped>
.panel {
  background: #f9fafb;
  border-radius: 12px;
  padding: 1rem;
}
.form-row {
  display: flex;
  gap: 0.5rem;
  margin: 1rem 0;
}
input {
  flex: 1;
  padding: 0.5rem;
}
button {
  background: #111827;
  color: white;
  border: none;
  border-radius: 8px;
  padding: 0.5rem 1rem;
}
</style>
