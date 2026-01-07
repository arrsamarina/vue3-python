<template>
  <footer class="app-footer">
    <div class="footer-content">
      <p>&copy; 2024 Task Manager. Vue 3 + FastAPI</p>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'AppFooter'
}
</script>

<style scoped>
.app-footer {
  background-color: #2c3e50;
  color: white;
  padding: 20px 0;
  margin-top: auto;
}

.footer-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  text-align: center;
}

.footer-content p {
  margin: 0;
  font-size: 14px;
}
</style>

