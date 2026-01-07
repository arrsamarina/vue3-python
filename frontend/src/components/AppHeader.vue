<template>
  <header class="app-header">
    <div class="header-content">
      <router-link to="/" class="logo">
        <h1>📋 Task Manager</h1>
      </router-link>
      <nav class="nav">
        <router-link to="/" class="nav-link">Главная</router-link>
        <router-link to="/tasks" class="nav-link">Задачи</router-link>
        <router-link to="/tasks/new" class="nav-link btn btn-primary btn-small">+ Новая задача</router-link>
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
  background-color: #2c3e50;
  color: white;
  padding: 15px 0;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
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
  color: white;
  text-decoration: none;
  padding: 8px 15px;
  border-radius: 5px;
  transition: background-color 0.3s;
}

.nav-link:hover {
  background-color: rgba(255,255,255,0.1);
}

.nav-link.router-link-active {
  background-color: #42b983;
}
</style>

