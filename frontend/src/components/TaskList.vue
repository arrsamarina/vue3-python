<template>
  <div class="task-list">
    <div class="filters-section">
      <div class="filter-group">
        <label>Фильтр по статусу:</label>
        <select v-model="statusFilter" class="filter-select">
          <option value="all">Все</option>
          <option value="completed">Выполненные</option>
          <option value="pending">Невыполненные</option>
        </select>
      </div>
      
      <div class="filter-group">
        <label>Сортировка:</label>
        <select v-model="sortBy" class="filter-select">
          <option value="date">По дате добавления</option>
          <option value="alphabet">По алфавиту</option>
        </select>
      </div>
    </div>

    <div v-if="loading" class="loading">Загрузка задач...</div>
    
    <div v-else-if="sortedTasks.length === 0" class="empty-state">
      <p>Нет задач для отображения</p>
      <router-link to="/tasks/new" class="btn btn-primary">Создать первую задачу</router-link>
    </div>
    
    <div v-else class="tasks-container">
      <TaskItem
        v-for="task in sortedTasks"
        :key="task.id"
        :task="task"
        @delete="handleDelete(task.id)"
        @toggle="handleToggle(task.id)"
        @edit="handleEdit(task.id)"
      />
    </div>
  </div>
</template>

<script>
import { ref, computed, watch, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import TaskItem from './TaskItem.vue'
import { taskService } from '../services/api'

export default {
  name: 'TaskList',
  components: {
    TaskItem
  },
  emits: ['task-updated'],
  setup(props, { emit }) {
    const router = useRouter()
    const tasks = ref([])
    const loading = ref(true)
    const statusFilter = ref('all')
    const sortBy = ref('date')

    // Computed свойство для фильтрации
    const filteredTasks = computed(() => {
      if (statusFilter.value === 'all') {
        return tasks.value
      } else if (statusFilter.value === 'completed') {
        return tasks.value.filter(task => task.completed)
      } else {
        return tasks.value.filter(task => !task.completed)
      }
    })

    // Computed свойство для сортировки
    const sortedTasks = computed(() => {
      const filtered = [...filteredTasks.value]
      if (sortBy.value === 'date') {
        return filtered.sort((a, b) => {
          const dateA = new Date(a.created_at || 0)
          const dateB = new Date(b.created_at || 0)
          return dateB - dateA // Новые сначала
        })
      } else if (sortBy.value === 'alphabet') {
        return filtered.sort((a, b) => a.title.localeCompare(b.title))
      }
      return filtered
    })

    // Watch для отслеживания изменений фильтров
    watch([statusFilter, sortBy], () => {
      console.log('Фильтры изменены:', { statusFilter: statusFilter.value, sortBy: sortBy.value })
    })

    const loadTasks = async () => {
      try {
        loading.value = true
        tasks.value = await taskService.getAllTasks()
      } catch (error) {
        console.error('Ошибка загрузки задач:', error)
        alert('Не удалось загрузить задачи')
      } finally {
        loading.value = false
      }
    }

    const handleDelete = async (id) => {
      if (confirm('Вы уверены, что хотите удалить эту задачу?')) {
        try {
          await taskService.deleteTask(id)
          await loadTasks()
          emit('task-updated')
        } catch (error) {
          console.error('Ошибка удаления задачи:', error)
          alert('Не удалось удалить задачу')
        }
      }
    }

    const handleToggle = async (id) => {
      try {
        const task = tasks.value.find(t => t.id === id)
        if (task) {
          await taskService.updateTask(id, {
            completed: !task.completed
          })
          await loadTasks()
          emit('task-updated')
        }
      } catch (error) {
        console.error('Ошибка изменения статуса:', error)
        alert('Не удалось изменить статус задачи')
      }
    }

    const handleEdit = (id) => {
      router.push({ name: 'task-edit', params: { id } })
    }

    onMounted(() => {
      loadTasks()
    })

    return {
      tasks,
      loading,
      statusFilter,
      sortBy,
      filteredTasks,
      sortedTasks,
      handleDelete,
      handleToggle,
      handleEdit
    }
  }
}
</script>

<style scoped>
.task-list {
  width: 100%;
}

.filters-section {
  display: flex;
  gap: 20px;
  margin-bottom: 20px;
  flex-wrap: wrap;
  padding: 20px;
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.filter-group {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.filter-group label {
  font-weight: 500;
  font-size: 14px;
}

.filter-select {
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 5px;
  font-size: 14px;
  min-width: 200px;
}

.loading {
  text-align: center;
  padding: 40px;
  font-size: 18px;
  color: #666;
}

.empty-state {
  text-align: center;
  padding: 60px 20px;
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.empty-state p {
  font-size: 18px;
  color: #666;
  margin-bottom: 20px;
}

.tasks-container {
  display: flex;
  flex-direction: column;
}
</style>

