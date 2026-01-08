<template>
  <div class="spinner-container">
    <div class="spinner"></div>
    <p v-if="text" class="spinner-text">{{ text }}</p>
  </div>
</template>

<script>
export default {
  name: 'Spinner',
  props: {
    text: {
      type: String,
      default: ''
    }
  }
}
</script>

<style scoped>
.spinner-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  gap: 16px;
}

.spinner {
  width: 48px;
  height: 48px;
  border: 4px solid #1a1a1a;
  border-top-color: #86efac;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

.spinner-text {
  color: #8b949e;
  font-size: 14px;
  font-weight: 500;
  margin: 0;
}
</style>

