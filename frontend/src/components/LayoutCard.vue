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
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  overflow: hidden;
  margin-bottom: 20px;
}

.card-header {
  padding: 20px;
  background-color: #f8f9fa;
  border-bottom: 1px solid #e9ecef;
}

.card-body {
  padding: 20px;
}

.card-footer {
  padding: 15px 20px;
  background-color: #f8f9fa;
  border-top: 1px solid #e9ecef;
}
</style>

