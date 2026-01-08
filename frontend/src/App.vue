<template>
  <div id="app">
    <AppHeader />
    <main class="main-content">
      <router-view />
    </main>
    <AppFooter />
  </div>
</template>

<script>
import AppHeader from './components/AppHeader.vue'
import AppFooter from './components/AppFooter.vue'

export default {
  name: 'App',
  components: {
    AppHeader,
    AppFooter
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
  background-color: #000000;
  color: #e6edf3;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

h1 {
  font-size: 2.5rem;
  font-weight: 700;
  line-height: 1.2;
  letter-spacing: -0.02em;
}

h2 {
  font-size: 2rem;
  font-weight: 600;
  line-height: 1.3;
  letter-spacing: -0.01em;
}

h3 {
  font-size: 1.5rem;
  font-weight: 600;
  line-height: 1.4;
}

p {
  line-height: 1.7;
}

#app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.main-content {
  flex: 1;
  padding: 112px 24px 32px;
  max-width: 1200px;
  width: 100%;
  margin: 0 auto;
  animation: fadeIn 0.4s ease-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (max-width: 768px) {
  .main-content {
    padding: 100px 16px 20px;
  }
}

.btn {
  padding: 12px 24px;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  font-size: 14px;
  font-weight: 500;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  text-decoration: none;
  display: inline-block;
  position: relative;
  overflow: hidden;
  box-shadow: 0 2px 4px rgba(0,0,0,0.2);
  text-align: center;
}

.btn::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 0;
  height: 0;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.3);
  transform: translate(-50%, -50%);
  transition: width 0.6s, height 0.6s;
}

.btn:active::before {
  width: 300px;
  height: 300px;
}

.btn-primary {
  background-color: #86efac;
  color: #0f172a;
}

.btn-primary:hover {
  background-color: #a7f3d0;
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(134, 239, 172, 0.3);
}

.btn-primary:active {
  transform: translateY(0);
}

.btn-danger {
  background-color: #fca5a5;
  color: #0f172a;
}

.btn-danger:hover {
  background-color: #fda4af;
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(252, 165, 165, 0.3);
}

.btn-danger:active {
  transform: translateY(0);
}

.btn-secondary {
  background-color: #cbd5e1;
  color: #0f172a;
}

.btn-secondary:hover {
  background-color: #e2e8f0;
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(203, 213, 225, 0.3);
}

.btn-secondary:active {
  transform: translateY(0);
}

.btn-small {
  padding: 8px 16px;
  font-size: 12px;
  border-radius: 8px;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  font-weight: 500;
  color: #e6edf3;
}

.form-group input,
.form-group textarea,
.form-group select {
  width: 100%;
  padding: 12px 50px 12px 16px;
  border: 2px solid #1a1a1a;
  border-radius: 10px;
  font-size: 14px;
  font-family: 'Montserrat', sans-serif;
  background-color: #0f0f0f;
  color: #e6edf3;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.form-group select {
  appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='14' height='14' viewBox='0 0 12 12'%3E%3Cpath fill='%238b949e' d='M6 9L1 4h10z'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 16px center;
  background-size: 14px;
  cursor: pointer;
}

.form-group select:focus {
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='14' height='14' viewBox='0 0 12 12'%3E%3Cpath fill='%2386efac' d='M6 9L1 4h10z'/%3E%3C/svg%3E");
}

.form-group select.select-open {
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='14' height='14' viewBox='0 0 12 12'%3E%3Cpath fill='%2386efac' d='M6 3L1 8h10z'/%3E%3C/svg%3E");
}

.form-group input::placeholder,
.form-group textarea::placeholder {
  color: #6b7280;
  opacity: 0.7;
  font-weight: 400;
}

.form-group textarea {
  min-height: 100px;
  resize: vertical;
}

.form-group input:focus,
.form-group textarea:focus,
.form-group select:focus {
  outline: none;
  border-color: #86efac;
  background-color: #121212;
  box-shadow: 0 0 0 3px rgba(134, 239, 172, 0.1), 0 0 20px rgba(134, 239, 172, 0.2);
  transform: translateY(-1px);
}

.form-group input:focus::placeholder,
.form-group textarea:focus::placeholder {
  opacity: 0.5;
}

.error-message {
  color: #fca5a5;
  font-size: 12px;
  margin-top: 8px;
  font-weight: 500;
  animation: slideDown 0.3s ease-out;
}

@keyframes slideDown {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.radio-group {
  display: flex;
  gap: 24px;
  margin-top: 12px;
  flex-wrap: wrap;
}

.radio-group label {
  display: flex;
  align-items: center;
  gap: 8px;
  font-weight: 500;
  cursor: pointer;
  color: #e6edf3;
  padding: 8px 12px;
  border-radius: 8px;
  transition: all 0.2s ease;
}

.radio-group label:hover {
  background-color: rgba(255, 255, 255, 0.05);
}

.radio-group input[type="radio"] {
  width: 18px;
  height: 18px;
  cursor: pointer;
  accent-color: #86efac;
  transition: all 0.2s ease;
}

.radio-group input[type="radio"]:checked {
  transform: scale(1.1);
}

.checkbox-group {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-top: 12px;
  padding: 8px 0;
}

.checkbox-group label {
  color: #e6edf3;
  font-weight: 500;
  cursor: pointer;
}

.checkbox-group input[type="checkbox"] {
  width: 20px;
  height: 20px;
  cursor: pointer;
  accent-color: #86efac;
  border-radius: 4px;
  transition: all 0.2s ease;
}

.checkbox-group input[type="checkbox"]:checked {
  transform: scale(1.1);
}
</style>

