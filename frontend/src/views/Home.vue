<template>
  <LayoutCard>
    <template #header>
      <h1>Добро пожаловать в Task Manager!</h1>
    </template>
    
    <template #default="{ data }">
      <div class="home-content">
        <p class="welcome-text">
          Это приложение поможет вам эффективно управлять вашими задачами.
          Вы можете создавать, редактировать, удалять задачи, а также фильтровать и сортировать их.
        </p>
        
        <div class="features">
          <h2>Возможности:</h2>
          <ul>
            <li>✅ Создание и управление задачами</li>
            <li>🔍 Фильтрация по статусу</li>
            <li>📊 Сортировка по дате и алфавиту</li>
            <li>⭐ Отметка важных задач</li>
            <li>📝 Редактирование задач</li>
            <li>🗑️ Удаление задач</li>
          </ul>
        </div>
        
        <div class="actions">
          <router-link to="/tasks" class="btn btn-primary btn-large">
            Перейти к задачам →
          </router-link>
        </div>
        
        <div class="info">
          <p><small>Данные карточки: {{ data.title }} - {{ data.timestamp }}</small></p>
        </div>
      </div>
    </template>
    
    <template #footer>
      <p class="footer-text">Начните работу с задачами прямо сейчас!</p>
    </template>
  </LayoutCard>
</template>

<script>
import LayoutCard from '../components/LayoutCard.vue'

export default {
  name: 'Home',
  components: {
    LayoutCard
  }
}
</script>

<style scoped>
.home-content {
  text-align: center;
}

.welcome-text {
  font-size: 18px;
  line-height: 1.6;
  color: #555;
  margin-bottom: 30px;
}

.features {
  text-align: left;
  max-width: 500px;
  margin: 0 auto 30px;
  background: #f8f9fa;
  padding: 20px;
  border-radius: 8px;
}

.features h2 {
  margin-bottom: 15px;
  color: #2c3e50;
}

.features ul {
  list-style: none;
  padding: 0;
}

.features li {
  padding: 8px 0;
  font-size: 16px;
}

.actions {
  margin: 30px 0;
}

.btn-large {
  padding: 15px 30px;
  font-size: 18px;
}

.info {
  margin-top: 20px;
  padding-top: 20px;
  border-top: 1px solid #e9ecef;
}

.footer-text {
  text-align: center;
  color: #666;
  font-style: italic;
}
</style>

