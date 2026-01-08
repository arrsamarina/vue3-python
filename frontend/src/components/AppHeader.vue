<template>
  <header class="app-header">
    <div class="header-content">
      <router-link to="/" class="logo">
        <h1>Task Manager</h1>
      </router-link>
      <nav class="nav">
        <router-link to="/" class="nav-link">Главная</router-link>
        <router-link to="/tasks" class="nav-link">Задачи</router-link>
      </nav>
    </div>
  </header>
</template>

<script>
export default {
  name: 'AppHeader'
}
</script>

<style scoped>
.app-header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  background-color: #0a0a0a;
  color: #e6edf3;
  padding: 16px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.5), 0 1px 2px rgba(0,0,0,0.3);
  border-bottom: 1px solid #1a1a1a;
  transition: all 0.3s ease;
}

@media (max-width: 768px) {
  .app-header {
    padding: 12px 0;
  }
  
  .nav {
    gap: 12px;
  }
  
  .nav-link {
    padding: 6px 12px;
    font-size: 13px;
  }
}

.header-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  text-decoration: none;
  color: white;
}

.logo h1 {
  font-size: 24px;
  font-weight: 600;
}

.nav {
  display: flex;
  gap: 20px;
  align-items: center;
}

.nav-link {
  color: #e6edf3;
  text-decoration: none;
  padding: 8px 15px;
  border-radius: 5px;
  transition: background-color 0.3s;
}

.nav-link:hover {
  background-color: rgba(255,255,255,0.08);
}

.nav-link.router-link-active {
  background-color: #86efac;
  color: #0f172a;
}

</style>

