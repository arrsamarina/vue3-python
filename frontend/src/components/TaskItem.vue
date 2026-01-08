<template>
  <div class="task-item" :class="{ completed: task.completed, important: task.important }">
    <div class="task-content">
      <div class="task-header">
        <h3 class="task-title">{{ task.title }}</h3>
        <div class="task-badges">
          <span class="badge priority" :class="task.priority">{{ getPriorityLabel(task.priority) }}</span>
          <span class="badge category">{{ getCategoryLabel(task.category) }}</span>
          <span v-if="task.important" class="badge important">ВАЖНО</span>
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
    // преобразование приоритета в читаемый формат
    getPriorityLabel(priority) {
      const labels = {
        low: 'НИЗКИЙ',
        medium: 'СРЕДНИЙ',
        high: 'ВЫСОКИЙ'
      }
      return labels[priority] || priority
    },
    // преобразование категории в читаемый формат
    getCategoryLabel(category) {
      const labels = {
        work: 'РАБОТА',
        personal: 'ЛИЧНОЕ',
        development: 'РАЗРАБОТКА'
      }
      return labels[category] || category
    },
    // форматирование даты в русский формат
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
  background: #0f0f0f;
  border-radius: 16px;
  padding: 24px;
  margin-bottom: 20px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.4), 0 1px 2px rgba(0,0,0,0.3);
  border: 1px solid #1a1a1a;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  border-left: 4px solid #86efac;
  animation: slideIn 0.4s ease-out;
  animation-fill-mode: both;
}

.task-item:nth-child(1) { animation-delay: 0.05s; }
.task-item:nth-child(2) { animation-delay: 0.1s; }
.task-item:nth-child(3) { animation-delay: 0.15s; }
.task-item:nth-child(4) { animation-delay: 0.2s; }
.task-item:nth-child(5) { animation-delay: 0.25s; }

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateX(-20px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.task-item:hover {
  box-shadow: 0 8px 24px rgba(0,0,0,0.6), 0 4px 8px rgba(0,0,0,0.4);
  border-color: #2a2a2a;
  transform: translateY(-2px);
}

.task-item.completed {
  opacity: 0.6;
  border-left-color: #6c757d;
}

.task-item.important {
  border-left-color: #fca5a5;
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
  font-size: 20px;
  font-weight: 600;
  color: #e6edf3;
  margin: 0;
  line-height: 1.4;
  letter-spacing: -0.01em;
}

.task-item.completed .task-title {
  text-decoration: line-through;
  color: #8b949e;
}

.task-badges {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.badge {
  padding: 6px 14px;
  border-radius: 20px;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.3px;
  text-transform: uppercase;
  box-shadow: 0 2px 4px rgba(0,0,0,0.2);
  transition: all 0.2s ease;
}

.badge:hover {
  transform: scale(1.05);
  box-shadow: 0 4px 8px rgba(0,0,0,0.3);
}

.badge.priority.low {
  background-color: #a7f3d0;
  color: #0f172a;
}

.badge.priority.medium {
  background-color: #fde68a;
  color: #0f172a;
}

.badge.priority.high {
  background-color: #fda4af;
  color: #0f172a;
}

.badge.category {
  background-color: #a5b4fc;
  color: #0f172a;
}

.badge.important {
  background-color: #fcd34d;
  color: #0f172a;
}

.task-description {
  color: #8b949e;
  margin-bottom: 16px;
  line-height: 1.7;
  font-size: 15px;
}

.task-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 12px;
  color: #8b949e;
  margin-top: 10px;
  margin-bottom: 20px;
  padding-bottom: 15px;
  border-bottom: 1px solid #1a1a1a;
}

.task-status {
  font-weight: 500;
}

.task-status.completed {
  color: #86efac;
}

.task-actions {
  display: flex;
  gap: 12px;
  margin-top: 0;
  flex-wrap: wrap;
}

.task-actions .btn {
  font-weight: 500;
  letter-spacing: 0.5px;
}

@media (max-width: 768px) {
  .task-item {
    padding: 20px;
  }
  
  .task-header {
    flex-direction: column;
    align-items: flex-start;
  }
  
  .task-badges {
    width: 100%;
    margin-top: 8px;
  }
  
  .task-actions {
    width: 100%;
  }
  
  .task-actions .btn {
    flex: 1;
    min-width: 0;
  }
}

@media (min-width: 768px) {
  .task-item {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
  }
  
  .task-meta {
    margin-bottom: 0;
    padding-bottom: 0;
    border-bottom: none;
  }
  
  .task-actions {
    margin-top: 0;
    flex-direction: column;
    margin-left: 20px;
  }
}
</style>

