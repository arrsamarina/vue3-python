<template>
  <div class="layout-card">
    <!-- Именованный слот header -->
    <header v-if="$slots.header" class="card-header">
      <slot name="header"></slot>
    </header>
    
    <!-- Обычный слот (default) с ограниченной областью видимости -->
    <div class="card-body">
      <slot :data="cardData">
        <!-- Контент по умолчанию, если слот не передан -->
        <p>Нет контента</p>
      </slot>
    </div>
    
    <!-- Именованный слот footer -->
    <footer v-if="$slots.footer" class="card-footer">
      <slot name="footer"></slot>
    </footer>
  </div>
</template>

<script>
import { ref } from 'vue'

export default {
  name: 'LayoutCard',
  setup() {
    const cardData = ref({
      title: 'Card Data',
      timestamp: new Date().toISOString()
    })
    
    return {
      cardData
    }
  }
}
</script>

<style scoped>
.layout-card {
  background: #0f0f0f;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.4), 0 1px 2px rgba(0,0,0,0.3);
  border: 1px solid #1a1a1a;
  overflow: hidden;
  margin-bottom: 24px;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  animation: fadeIn 0.4s ease-out;
}

.layout-card:hover {
  box-shadow: 0 4px 16px rgba(0,0,0,0.5), 0 2px 4px rgba(0,0,0,0.4);
}

.card-header {
  padding: 24px;
  background-color: #121212;
  border-bottom: 1px solid #1a1a1a;
}

.card-header h1,
.card-header h2 {
  color: #e6edf3;
  margin: 0;
}

.card-body {
  padding: 24px;
  color: #e6edf3;
}

.card-footer {
  padding: 20px 24px;
  background-color: #121212;
  border-top: 1px solid #1a1a1a;
  color: #8b949e;
}

@media (max-width: 768px) {
  .card-header,
  .card-body,
  .card-footer {
    padding: 20px;
  }
}
</style>

