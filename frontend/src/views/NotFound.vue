<template>
  <LayoutCard>
    <template #header>
      <h1>404 - Страница не найдена</h1>
    </template>
    
    <template #default>
      <div class="not-found-content">
        <div class="error-icon">🔍</div>
        <p class="error-message">
          К сожалению, запрашиваемая страница не существует.
        </p>
        <p class="error-description">
          Возможно, вы перешли по неверной ссылке или страница была удалена.
        </p>
        <div class="actions">
          <router-link to="/" class="btn btn-primary">На главную</router-link>
          <router-link to="/tasks" class="btn btn-secondary">К задачам</router-link>
        </div>
      </div>
    </template>
  </LayoutCard>
</template>

<script>
import LayoutCard from '../components/LayoutCard.vue'

export default {
  name: 'NotFound',
  components: {
    LayoutCard
  }
}
</script>

<style scoped>
.not-found-content {
  text-align: center;
  padding: 40px 20px;
}

.error-icon {
  font-size: 80px;
  margin-bottom: 20px;
}

.error-message {
  font-size: 24px;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 15px;
}

.error-description {
  font-size: 16px;
  color: #666;
  margin-bottom: 30px;
}

.actions {
  display: flex;
  gap: 15px;
  justify-content: center;
  flex-wrap: wrap;
}
</style>

