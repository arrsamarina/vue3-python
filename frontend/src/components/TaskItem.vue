<template>
  <div class="task-item" :class="{ completed: task.completed, important: task.important }">
    <div class="task-content">
      <div class="task-header">
        <h3 class="task-title">{{ task.title }}</h3>
        <div class="task-badges">
          <span class="badge priority" :class="task.priority">{{ getPriorityLabel(task.priority) }}</span>
          <span class="badge category">{{ getCategoryLabel(task.category) }}</span>
          <span v-if="task.important" class="badge important">⭐ Важно</span>
        </div>
      </div>
      <p class="task-description">{{ task.description }}</p>
      <div class="task-meta">
        <span class="task-date">Создано: {{ formatDate(task.created_at) }}</span>
        <span class="task-status" :class="{ completed: task.completed }">
          {{ task.completed ? '✓ Выполнено' : '○ В работе' }}
        </span>
      </div>
    </div>
    <div class="task-actions">
      <button @click="$emit('toggle')" class="btn btn-small" :class="task.completed ? 'btn-secondary' : 'btn-primary'">
        {{ task.completed ? 'Отменить' : 'Выполнить' }}
      </button>
      <button @click="$emit('edit')" class="btn btn-small btn-secondary">Редактировать</button>
      <button @click="$emit('delete')" class="btn btn-small btn-danger">Удалить</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TaskItem',
  props: {
    task: {
      type: Object,
      required: true
    }
  },
  emits: ['toggle', 'edit', 'delete'],
  methods: {
    getPriorityLabel(priority) {
      const labels = {
        low: 'Низкий',
        medium: 'Средний',
        high: 'Высокий'
      }
      return labels[priority] || priority
    },
    getCategoryLabel(category) {
      const labels = {
        work: 'Работа',
        personal: 'Личное',
        development: 'Разработка'
      }
      return labels[category] || category
    },
    formatDate(dateString) {
      if (!dateString) return ''
      const date = new Date(dateString)
      return date.toLocaleDateString('ru-RU', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
      })
    }
  }
}
</script>

<style scoped>
.task-item {
  background: white;
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 15px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  transition: all 0.3s;
  border-left: 4px solid #42b983;
}

.task-item:hover {
  box-shadow: 0 4px 8px rgba(0,0,0,0.15);
}

.task-item.completed {
  opacity: 0.7;
  border-left-color: #6c757d;
}

.task-item.important {
  border-left-color: #e74c3c;
}

.task-content {
  flex: 1;
}

.task-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 10px;
  flex-wrap: wrap;
  gap: 10px;
}

.task-title {
  font-size: 18px;
  font-weight: 600;
  color: #2c3e50;
  margin: 0;
}

.task-item.completed .task-title {
  text-decoration: line-through;
  color: #6c757d;
}

.task-badges {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.badge {
  padding: 4px 10px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 500;
}

.badge.priority.low {
  background-color: #d4edda;
  color: #155724;
}

.badge.priority.medium {
  background-color: #fff3cd;
  color: #856404;
}

.badge.priority.high {
  background-color: #f8d7da;
  color: #721c24;
}

.badge.category {
  background-color: #e7f3ff;
  color: #004085;
}

.badge.important {
  background-color: #ffeaa7;
  color: #856404;
}

.task-description {
  color: #555;
  margin-bottom: 15px;
  line-height: 1.5;
}

.task-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 12px;
  color: #888;
  margin-top: 10px;
}

.task-status {
  font-weight: 500;
}

.task-status.completed {
  color: #42b983;
}

.task-actions {
  display: flex;
  gap: 10px;
  margin-top: 15px;
  flex-wrap: wrap;
}

@media (min-width: 768px) {
  .task-item {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
  }
  
  .task-actions {
    margin-top: 0;
    flex-direction: column;
  }
}
</style>

