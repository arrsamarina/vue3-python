<template>
  <LayoutCard>
    <template #header>
      <h2>{{ isEdit ? 'Редактирование задачи' : 'Создание новой задачи' }}</h2>
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

    // Watch для валидации
    watch(() => formData.title, (newVal) => {
      if (newVal.length < 3) {
        errors.title = 'Заголовок должен содержать минимум 3 символа'
      } else {
        errors.title = ''
      }
    })

    watch(() => formData.description, (newVal) => {
      if (newVal.length < 10) {
        errors.description = 'Описание должно содержать минимум 10 символов'
      } else {
        errors.description = ''
      }
    })

    const loadTask = async () => {
      if (!isEdit.value) return
      
      try {
        loading.value = true
        const task = await taskService.getTaskById(taskId.value)
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
.form-textarea,
.form-select {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  font-size: 14px;
  font-family: inherit;
}

.form-input.error,
.form-textarea.error {
  border-color: #e74c3c;
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
</style>

