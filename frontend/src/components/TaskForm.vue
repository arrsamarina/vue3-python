<template>
  <LayoutCard>
    <template #header>
      <h2>{{ isEdit ? 'Редактирование задачи' : 'Новая задача' }}</h2>
    </template>
    
    <template #default>
      <form @submit.prevent="handleSubmit" class="task-form">
        <div class="form-group">
          <label for="title">Заголовок *</label>
          <input
            id="title"
            v-model.trim="formData.title"
            type="text"
            required
            placeholder="Введите заголовок задачи"
            class="form-input"
            :class="{ error: errors.title }"
          />
          <span v-if="errors.title" class="error-message">{{ errors.title }}</span>
        </div>

        <div class="form-group">
          <label for="description">Описание *</label>
          <textarea
            id="description"
            v-model.trim="formData.description"
            required
            placeholder="Введите описание задачи"
            class="form-textarea"
            :class="{ error: errors.description }"
          ></textarea>
          <span v-if="errors.description" class="error-message">{{ errors.description }}</span>
        </div>

        <div class="form-group">
          <label for="priority">Приоритет *</label>
          <select
            id="priority"
            v-model="formData.priority"
            required
            class="form-select"
            :class="{ 'select-open': prioritySelectOpen }"
            @focus="prioritySelectOpen = true"
            @blur="prioritySelectOpen = false"
            @change="prioritySelectOpen = false"
          >
            <option value="low">Низкий</option>
            <option value="medium">Средний</option>
            <option value="high">Высокий</option>
          </select>
        </div>

        <div class="form-group">
          <label>Категория *</label>
          <div class="radio-group">
            <label>
              <input
                type="radio"
                v-model="formData.category"
                value="work"
                required
              />
              Работа
            </label>
            <label>
              <input
                type="radio"
                v-model="formData.category"
                value="personal"
                required
              />
              Личное
            </label>
            <label>
              <input
                type="radio"
                v-model="formData.category"
                value="development"
                required
              />
              Разработка
            </label>
          </div>
        </div>

        <div class="form-group">
          <div class="checkbox-group">
            <input
              type="checkbox"
              id="important"
              v-model="formData.important"
            />
            <label for="important">Важно</label>
          </div>
        </div>

        <div class="form-actions">
          <button type="submit" class="btn btn-primary" :disabled="loading">
            {{ loading ? 'Сохранение...' : (isEdit ? 'Сохранить изменения' : 'Создать задачу') }}
          </button>
          <router-link to="/tasks" class="btn btn-secondary">Отмена</router-link>
        </div>
      </form>
    </template>
  </LayoutCard>
</template>

<script>
import { ref, reactive, watch, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import LayoutCard from './LayoutCard.vue'
import { taskService } from '../services/api'

export default {
  name: 'TaskForm',
  components: {
    LayoutCard
  },
  props: {
    taskId: {
      type: [String, Number],
      default: null
    }
  },
  setup(props) {
    const router = useRouter()
    const route = useRoute()
    const loading = ref(false)
    const isEdit = ref(!!props.taskId || !!route.params.id)
    const taskId = ref(props.taskId || route.params.id)
    const prioritySelectOpen = ref(false)

    const formData = reactive({
      title: '',
      description: '',
      priority: 'medium',
      category: 'work',
      important: false
    })

    const errors = reactive({
      title: '',
      description: ''
    })

    // валидация заголовка при вводе
    watch(() => formData.title, (newVal) => {
      if (newVal.length < 3) {
        errors.title = 'Заголовок должен содержать минимум 3 символа'
      } else {
        errors.title = ''
      }
    })

    // валидация описания при вводе
    watch(() => formData.description, (newVal) => {
      if (newVal.length < 10) {
        errors.description = 'Описание должно содержать минимум 10 символов'
      } else {
        errors.description = ''
      }
    })

    // загрузка задачи для редактирования
    const loadTask = async () => {
      if (!isEdit.value) return
      
      try {
        loading.value = true
        const task = await taskService.getTaskById(taskId.value)
        // заполнение формы данными задачи
        Object.assign(formData, {
          title: task.title,
          description: task.description,
          priority: task.priority,
          category: task.category,
          important: task.important
        })
      } catch (error) {
        console.error('Ошибка загрузки задачи:', error)
        alert('Не удалось загрузить задачу')
        router.push('/tasks')
      } finally {
        loading.value = false
      }
    }

    // валидация формы перед отправкой
    const validateForm = () => {
      errors.title = ''
      errors.description = ''

      if (formData.title.length < 3) {
        errors.title = 'Заголовок должен содержать минимум 3 символа'
        return false
      }

      if (formData.description.length < 10) {
        errors.description = 'Описание должно содержать минимум 10 символов'
        return false
      }

      return true
    }

    // обработка отправки формы (создание или обновление задачи)
    const handleSubmit = async () => {
      if (!validateForm()) {
        return
      }

      try {
        loading.value = true
        
        if (isEdit.value) {
          await taskService.updateTask(taskId.value, formData)
        } else {
          await taskService.createTask(formData)
        }
        
        router.push('/tasks')
      } catch (error) {
        console.error('Ошибка сохранения задачи:', error)
        alert('Не удалось сохранить задачу')
      } finally {
        loading.value = false
      }
    }

    onMounted(() => {
      if (isEdit.value) {
        loadTask()
      }
    })

    return {
      formData,
      errors,
      loading,
      isEdit,
      prioritySelectOpen,
      handleSubmit
    }
  }
}
</script>

<style scoped>
.task-form {
  max-width: 600px;
}

.form-input,
.form-textarea {
  width: 100%;
  padding: 12px 16px;
  border: 2px solid #1a1a1a;
  border-radius: 10px;
  font-size: 14px;
  font-family: 'Montserrat', sans-serif;
  background-color: #0f0f0f;
  color: #e6edf3;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.form-select {
  width: 100%;
  padding: 12px 50px 12px 16px;
  border: 2px solid #1a1a1a;
  border-radius: 10px;
  font-size: 14px;
  font-family: 'Montserrat', sans-serif;
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

.form-select:focus {
  outline: none;
  border-color: #86efac;
  background-color: #121212;
  box-shadow: 0 0 0 3px rgba(134, 239, 172, 0.1), 0 0 20px rgba(134, 239, 172, 0.2);
  transform: translateY(-1px);
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='14' height='14' viewBox='0 0 12 12'%3E%3Cpath fill='%2386efac' d='M6 9L1 4h10z'/%3E%3C/svg%3E");
}

.form-select.select-open {
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='14' height='14' viewBox='0 0 12 12'%3E%3Cpath fill='%2386efac' d='M6 3L1 8h10z'/%3E%3C/svg%3E");
}

.form-input::placeholder,
.form-textarea::placeholder {
  color: #6b7280;
  opacity: 0.7;
  font-weight: 400;
}

.form-input:focus,
.form-textarea:focus {
  outline: none;
  border-color: #86efac;
  background-color: #121212;
  box-shadow: 0 0 0 3px rgba(134, 239, 172, 0.1), 0 0 20px rgba(134, 239, 172, 0.2);
  transform: translateY(-1px);
}

.form-select:focus,
.form-select.select-open {
  outline: none;
  border-color: #86efac;
  background-color: #121212;
  box-shadow: 0 0 0 3px rgba(134, 239, 172, 0.1), 0 0 20px rgba(134, 239, 172, 0.2);
  transform: translateY(-1px);
}

.form-input:focus::placeholder,
.form-textarea:focus::placeholder {
  opacity: 0.5;
}

.form-input.error,
.form-textarea.error {
  border-color: #fca5a5;
  box-shadow: 0 0 0 3px rgba(252, 165, 165, 0.1), 0 0 20px rgba(252, 165, 165, 0.2);
}

.form-textarea {
  min-height: 100px;
  resize: vertical;
}

.form-actions {
  display: flex;
  gap: 10px;
  margin-top: 30px;
}

.form-actions .btn {
  flex: 1;
}

/* выравнивание radio и checkbox групп с остальными полями */
.task-form :deep(.radio-group) {
  margin-top: 0;
  margin-left: 0;
  margin-right: 0;
}

.task-form :deep(.checkbox-group) {
  margin-top: 0;
  padding: 0;
}
</style>

