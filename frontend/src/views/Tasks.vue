<template>
  <div class="tasks-page">
    <div class="page-header">
      <h1>Список задач</h1>
      <router-link to="/tasks/new" class="btn btn-primary">
        + Создать задачу
      </router-link>
    </div>
    
    <TaskList @task-updated="handleTaskUpdated" />
  </div>
</template>

<script>
import { ref } from 'vue'
import TaskList from '../components/TaskList.vue'

export default {
  name: 'Tasks',
  components: {
    TaskList
  },
  setup() {
    const handleTaskUpdated = () => {
      // Можно добавить логику обновления, если нужно
      console.log('Задача обновлена')
    }

    return {
      handleTaskUpdated
    }
  }
}
</script>

<style scoped>
.tasks-page {
  width: 100%;
}

.page-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
  flex-wrap: wrap;
  gap: 15px;
}

.page-header h1 {
  font-size: 32px;
  color: #2c3e50;
  margin: 0;
}

@media (max-width: 768px) {
  .page-header {
    flex-direction: column;
    align-items: flex-start;
  }
}
</style>

