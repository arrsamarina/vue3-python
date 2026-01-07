<template>
  <div class="task-edit-page">
    <TaskForm :task-id="taskId" />
  </div>
</template>

<script>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import TaskForm from '../components/TaskForm.vue'

export default {
  name: 'TaskEdit',
  components: {
    TaskForm
  },
  setup() {
    const route = useRoute()
    const taskId = computed(() => route.params.id)

    return {
      taskId
    }
  }
}
</script>

<style scoped>
.task-edit-page {
  width: 100%;
  max-width: 800px;
  margin: 0 auto;
}
</style>

