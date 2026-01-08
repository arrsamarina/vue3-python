<template>
  <div class="tasks-page">
    <div class="page-header">
      <h1>Список задач</h1>
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
  margin-bottom: 32px;
  flex-wrap: wrap;
  gap: 20px;
  animation: fadeIn 0.4s ease-out;
}

.page-header h1 {
  font-size: 2.5rem;
  color: #e6edf3;
  margin: 0;
  font-weight: 700;
  letter-spacing: -0.02em;
}

.page-header .btn-primary {
  background-color: transparent;
  border: 2px solid #86efac;
  color: #e6edf3;
}

.page-header .btn-primary:hover {
  background-color: transparent;
  border-color: #a7f3d0;
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(134, 239, 172, 0.3);
}

@media (max-width: 768px) {
  .page-header {
    flex-direction: column;
    align-items: flex-start;
    margin-bottom: 24px;
    gap: 16px;
  }
  
  .page-header h1 {
    font-size: 2rem;
  }
  
  .page-header .btn {
    width: 100%;
    justify-content: center;
  }
}
</style>

