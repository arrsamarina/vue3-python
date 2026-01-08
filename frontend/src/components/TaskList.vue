<template>
  <div class="task-list">
    <div class="filters-section">
      <div class="filter-group">
        <label>Фильтр по статусу:</label>
        <select 
          v-model="statusFilter" 
          class="filter-select"
          :class="{ 'select-open': statusSelectOpen }"
          @focus="statusSelectOpen = true"
          @blur="handleStatusBlur"
          @change="handleStatusChange"
        >
          <option value="all">Все</option>
          <option value="completed">Выполненные</option>
          <option value="pending">Невыполненные</option>
        </select>
      </div>
      
      <div class="filter-group">
        <label>Сортировка:</label>
        <select 
          v-model="sortBy" 
          class="filter-select"
          :class="{ 'select-open': sortSelectOpen }"
          @focus="sortSelectOpen = true"
          @blur="handleSortBlur"
          @change="handleSortChange"
        >
          <option value="date">По&nbsp;дате добавления</option>
          <option value="alphabet">По&nbsp;алфавиту</option>
        </select>
      </div>
      
      <div class="filter-actions">
        <router-link to="/tasks/new" class="btn btn-create-task">
          Создать задачу
        </router-link>
      </div>
    </div>

    <SkeletonLoader v-if="loading" :count="3" />
    
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
import { ref, computed, watch, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import TaskItem from './TaskItem.vue'
import SkeletonLoader from './SkeletonLoader.vue'
import Spinner from './Spinner.vue'
import { taskService } from '../services/api'

export default {
  name: 'TaskList',
  components: {
    TaskItem,
    SkeletonLoader,
    Spinner
  },
  emits: ['task-updated'],
  setup(props, { emit }) {
    const router = useRouter()
    const tasks = ref([])
    const loading = ref(true)
    const statusFilter = ref('all')
    const sortBy = ref('date')
    const statusSelectOpen = ref(false)
    const sortSelectOpen = ref(false)

    // фильтрация задач по статусу
    const filteredTasks = computed(() => {
      if (statusFilter.value === 'all') {
        return tasks.value
      } else if (statusFilter.value === 'completed') {
        return tasks.value.filter(task => task.completed)
      } else {
        return tasks.value.filter(task => !task.completed)
      }
    })

    // сортировка отфильтрованных задач
    const sortedTasks = computed(() => {
      const filtered = [...filteredTasks.value]
      if (sortBy.value === 'date') {
        // сортировка по дате создания (новые сначала)
        return filtered.sort((a, b) => {
          const dateA = new Date(a.created_at || 0)
          const dateB = new Date(b.created_at || 0)
          return dateB - dateA
        })
      } else if (sortBy.value === 'alphabet') {
        // сортировка по алфавиту
        return filtered.sort((a, b) => a.title.localeCompare(b.title))
      }
      return filtered
    })

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

    const handleStatusBlur = () => {
      // задержка для корректной обработки закрытия select браузером
      setTimeout(() => {
        statusSelectOpen.value = false
      }, 100)
    }

    const handleStatusChange = () => {
      statusSelectOpen.value = false
    }

    const handleSortBlur = () => {
      setTimeout(() => {
        sortSelectOpen.value = false
      }, 100)
    }

    const handleSortChange = () => {
      sortSelectOpen.value = false
    }

    // закрытие select при клике вне его области
    const handleClickOutside = (event) => {
      const target = event.target
      if (!target.closest('.filter-select')) {
        statusSelectOpen.value = false
        sortSelectOpen.value = false
      }
    }

    onMounted(() => {
      loadTasks()
      document.addEventListener('click', handleClickOutside)
    })

    onUnmounted(() => {
      document.removeEventListener('click', handleClickOutside)
    })

    return {
      tasks,
      loading,
      statusFilter,
      sortBy,
      statusSelectOpen,
      sortSelectOpen,
      filteredTasks,
      sortedTasks,
      handleDelete,
      handleToggle,
      handleEdit,
      handleStatusBlur,
      handleStatusChange,
      handleSortBlur,
      handleSortChange,
      handleClickOutside
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
  gap: 24px;
  margin-bottom: 24px;
  flex-wrap: wrap;
  padding: 0;
}

.filter-group {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.filter-group label {
  font-weight: 500;
  font-size: 14px;
  color: #e6edf3;
}

.filter-actions {
  display: flex;
  align-items: flex-end;
  margin-left: auto;
}

.filter-actions .btn-create-task {
  color: #e6edf3;
  background-color: transparent;
  border: 2px solid #86efac;
  white-space: nowrap;
}

.filter-actions .btn-create-task:hover {
  background-color: transparent;
  border-color: #a7f3d0;
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(134, 239, 172, 0.3);
}

.filter-select {
  padding: 10px 50px 10px 14px;
  border: 2px solid #1a1a1a;
  border-radius: 10px;
  font-size: 14px;
  font-family: 'Montserrat', sans-serif;
  min-width: 220px;
  background-color: #0f0f0f;
  color: #e6edf3;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='14' height='14' viewBox='0 0 12 12'%3E%3Cpath fill='%238b949e' d='M6 9L1 4h10z'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 16px center;
  background-size: 14px;
  cursor: pointer;
}

.filter-select:focus:not(.select-open) {
  outline: none;
  border-color: #86efac;
  background-color: #121212;
  box-shadow: 0 0 0 3px rgba(134, 239, 172, 0.1), 0 0 20px rgba(134, 239, 172, 0.2);
  transform: translateY(-1px);
}

.filter-select.select-open {
  outline: none;
  border-color: #86efac;
  background-color: #121212;
  box-shadow: 0 0 0 3px rgba(134, 239, 172, 0.1), 0 0 20px rgba(134, 239, 172, 0.2);
  transform: translateY(-1px);
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='14' height='14' viewBox='0 0 12 12'%3E%3Cpath fill='%2386efac' d='M6 3L1 8h10z'/%3E%3C/svg%3E") !important;
}


.empty-state {
  text-align: center;
  padding: 80px 24px;
  background: #0f0f0f;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.4), 0 1px 2px rgba(0,0,0,0.3);
  border: 1px solid #1a1a1a;
  animation: fadeIn 0.4s ease-out;
}

.empty-state p {
  font-size: 18px;
  color: #8b949e;
  margin-bottom: 20px;
}

.tasks-container {
  display: flex;
  flex-direction: column;
  animation: fadeIn 0.4s ease-out;
}

.filter-actions {
  display: flex;
  align-items: flex-end;
  margin-left: auto;
}

.filter-actions .btn-create-task {
  color: #e6edf3;
  background-color: transparent;
  border: 2px solid #86efac;
  white-space: nowrap;
}

.filter-actions .btn-create-task:hover {
  background-color: transparent;
  border-color: #a7f3d0;
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(134, 239, 172, 0.3);
}

@media (max-width: 768px) {
  .filters-section {
    gap: 16px;
  }
  
  .filter-select {
    min-width: 100%;
  }
  
  .filter-actions {
    margin-left: 0;
    width: 100%;
  }
  
  .filter-actions .btn-create-task {
    width: 100%;
  }
}
</style>

