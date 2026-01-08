<template>
  <div class="home-page">
    <div class="hero-section">
      <div class="hero-content">
        <h1 class="hero-title">
          <span class="title-accent">Управляйте</span> задачами
          <br>с&nbsp;легкостью
        </h1>
        <p class="hero-description">
          Современный Task Manager поможет вам организовать работу, 
          отслеживать прогресс и&nbsp;не упускать важные дела
        </p>
        <div class="hero-actions">
          <router-link to="/tasks" class="btn btn-hero-primary">
            Начать работу
            <span class="btn-arrow">→</span>
          </router-link>
        </div>
      </div>
    </div>

    <div class="features-grid">
      <div class="feature-card" v-for="(feature, index) in features" :key="index">
        <div class="feature-icon" :style="{ background: feature.color }">
          <span class="icon-symbol">{{ feature.icon }}</span>
        </div>
        <h3 class="feature-title">{{ feature.title }}</h3>
        <p class="feature-description">{{ feature.description }}</p>
      </div>
    </div>

    <LayoutCard>
      <template #header>
        <h2>Как это работает</h2>
      </template>
      
      <template #default="{ data }">
        <div class="workflow-section">
          <div class="workflow-steps">
            <div class="workflow-step">
              <div class="step-number">1</div>
              <div class="step-content">
                <h3>Создайте задачу</h3>
                <p>Добавьте заголовок, описание, приоритет и&nbsp;категорию</p>
              </div>
            </div>
            <div class="workflow-step">
              <div class="step-number">2</div>
              <div class="step-content">
                <h3>Организуйте</h3>
                <p>Используйте фильтры и&nbsp;сортировку для удобной навигации</p>
              </div>
            </div>
            <div class="workflow-step">
              <div class="step-number">3</div>
              <div class="step-content">
                <h3>Выполняйте</h3>
                <p>Отмечайте выполненные задачи и&nbsp;отслеживайте прогресс</p>
              </div>
            </div>
          </div>
        </div>
      </template>
      
      <template #footer>
        <div class="footer-cta">
          <p>Готовы начать? Создайте первую задачу прямо сейчас!</p>
          <router-link to="/tasks/new" class="btn btn-create-task">Создать задачу</router-link>
        </div>
      </template>
    </LayoutCard>
  </div>
</template>

<script>
import { ref } from 'vue'
import LayoutCard from '../components/LayoutCard.vue'

export default {
  name: 'Home',
  components: {
    LayoutCard
  },
  setup() {
    const features = ref([
      {
        icon: '✓',
        title: 'Управление задачами',
        description: 'Создавайте, редактируйте и&nbsp;удаляйте задачи в&nbsp;удобном интерфейсе',
        color: 'linear-gradient(135deg, #86efac 0%, #a7f3d0 100%)'
      },
      {
        icon: '⌕',
        title: 'Умная фильтрация',
        description: 'Фильтруйте задачи по&nbsp;статусу и&nbsp;находите нужное за&nbsp;секунды',
        color: 'linear-gradient(135deg, #a5b4fc 0%, #c7d2fe 100%)'
      },
      {
        icon: '⇅',
        title: 'Гибкая сортировка',
        description: 'Сортируйте по&nbsp;дате или&nbsp;алфавиту для оптимальной организации',
        color: 'linear-gradient(135deg, #fde68a 0%, #fef3c7 100%)'
      },
      {
        icon: '★',
        title: 'Приоритеты',
        description: 'Отмечайте важные задачи и&nbsp;устанавливайте приоритеты',
        color: 'linear-gradient(135deg, #fda4af 0%, #fecdd3 100%)'
      }
    ])

    return {
      features
    }
  }
}
</script>

<style scoped>
.home-page {
  width: 100%;
  animation: fadeIn 0.6s ease-out;
}

.hero-section {
  background: linear-gradient(135deg, #0f0f0f 0%, #1a1a1a 100%);
  border-radius: 24px;
  padding: 80px 40px;
  margin-bottom: 48px;
  text-align: center;
  border: 1px solid #1a1a1a;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
  position: relative;
  overflow: hidden;
}

.hero-section::before {
  content: '';
  position: absolute;
  top: -50%;
  right: -50%;
  width: 200%;
  height: 200%;
  background: radial-gradient(circle, rgba(134, 239, 172, 0.05) 0%, transparent 70%);
  animation: pulse 8s ease-in-out infinite;
}

@keyframes pulse {
  0%, 100% {
    transform: scale(1);
    opacity: 0.5;
  }
  50% {
    transform: scale(1.1);
    opacity: 0.8;
  }
}

.hero-content {
  position: relative;
  z-index: 1;
  max-width: 700px;
  margin: 0 auto;
}

.hero-title {
  font-size: 3.5rem;
  font-weight: 700;
  line-height: 1.1;
  margin-bottom: 24px;
  color: #e6edf3;
  letter-spacing: -0.03em;
}

.title-accent {
  background: linear-gradient(135deg, #86efac 0%, #a7f3d0 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-description {
  font-size: 1.25rem;
  line-height: 1.6;
  color: #8b949e;
  margin-bottom: 40px;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}

.hero-actions {
  display: flex;
  justify-content: center;
  gap: 16px;
}

.btn-hero-primary {
  padding: 16px 40px;
  font-size: 18px;
  font-weight: 600;
  background: linear-gradient(135deg, #86efac 0%, #a7f3d0 100%);
  color: #0f172a;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 4px 16px rgba(134, 239, 172, 0.3);
}

.btn-hero-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(134, 239, 172, 0.4);
}

.btn-arrow {
  transition: transform 0.3s ease;
}

.btn-hero-primary:hover .btn-arrow {
  transform: translateX(4px);
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px;
  margin-bottom: 48px;
}

.feature-card {
  background: #0f0f0f;
  border-radius: 16px;
  padding: 32px;
  border: 1px solid #1a1a1a;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  animation: fadeInUp 0.6s ease-out backwards;
}

.feature-card:nth-child(1) { animation-delay: 0.1s; }
.feature-card:nth-child(2) { animation-delay: 0.2s; }
.feature-card:nth-child(3) { animation-delay: 0.3s; }
.feature-card:nth-child(4) { animation-delay: 0.4s; }

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.feature-card:hover {
  transform: translateY(-4px);
  border-color: #2a2a2a;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5);
}

.feature-icon {
  width: 64px;
  height: 64px;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 20px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3);
}

.icon-symbol {
  font-size: 32px;
  color: #0f172a;
  filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.3));
}

.feature-title {
  font-size: 1.25rem;
  font-weight: 600;
  color: #e6edf3;
  margin-bottom: 12px;
  letter-spacing: -0.01em;
}

.feature-description {
  font-size: 14px;
  line-height: 1.6;
  color: #8b949e;
}

.workflow-section {
  padding: 20px 0;
}

.workflow-steps {
  display: flex;
  flex-direction: column;
  gap: 32px;
}

.workflow-step {
  display: flex;
  gap: 24px;
  align-items: flex-start;
  padding: 24px;
  background: #121212;
  border-radius: 12px;
  border: 1px solid #1a1a1a;
  transition: all 0.3s ease;
}

.workflow-step:hover {
  border-color: #2a2a2a;
  transform: translateX(4px);
}

.step-number {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  background: linear-gradient(135deg, #86efac 0%, #a7f3d0 100%);
  color: #0f172a;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  font-weight: 700;
  flex-shrink: 0;
  box-shadow: 0 4px 12px rgba(134, 239, 172, 0.3);
}

.step-content h3 {
  font-size: 1.25rem;
  font-weight: 600;
  color: #e6edf3;
  margin-bottom: 8px;
  letter-spacing: -0.01em;
}

.step-content p {
  font-size: 15px;
  line-height: 1.6;
  color: #8b949e;
  margin: 0;
}

.footer-cta {
  text-align: center;
  padding: 20px 0;
}

/* убираем фон у footer для этого блока */
.home-page :deep(.card-footer) {
  background-color: transparent;
  border-top: none;
  padding: 0;
}

.footer-cta p {
  color: #8b949e;
  font-size: 18px;
  margin-bottom: 24px;
  font-weight: 500;
}

.footer-cta .btn-create-task {
  color: #e6edf3;
  background-color: transparent;
  border: 3px solid #86efac;
  padding: 18px 48px;
  font-size: 18px;
  font-weight: 600;
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(134, 239, 172, 0.4);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.footer-cta .btn-create-task:hover {
  background-color: transparent;
  border-color: #a7f3d0;
  transform: translateY(-3px);
  box-shadow: 0 8px 24px rgba(134, 239, 172, 0.5), 0 0 20px rgba(134, 239, 172, 0.3);
}

@media (max-width: 768px) {
  .hero-section {
    padding: 60px 24px;
  }

  .hero-title {
    font-size: 2.5rem;
  }

  .hero-description {
    font-size: 1.1rem;
  }

  .features-grid {
    grid-template-columns: 1fr;
  }

  .workflow-step {
    flex-direction: column;
    align-items: center;
    text-align: center;
  }

  .workflow-step:hover {
    transform: translateY(-2px);
  }
}
</style>

