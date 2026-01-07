<template>
  <div class="task-new-page">
    <TaskForm />
  </div>
</template>

<script>
import TaskForm from '../components/TaskForm.vue'

export default {
  name: 'TaskNew',
  components: {
    TaskForm
  }
}
</script>

<style scoped>
.task-new-page {
  width: 100%;
  max-width: 800px;
  margin: 0 auto;
}
</style>

