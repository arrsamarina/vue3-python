<template>
  <div class="skeleton-container">
    <div v-for="n in count" :key="n" class="skeleton-item">
      <div class="skeleton-header">
        <div class="skeleton-line skeleton-title"></div>
        <div class="skeleton-badges">
          <div class="skeleton-badge"></div>
          <div class="skeleton-badge"></div>
        </div>
      </div>
      <div class="skeleton-line skeleton-description"></div>
      <div class="skeleton-line skeleton-description short"></div>
      <div class="skeleton-meta">
        <div class="skeleton-line skeleton-meta-line"></div>
        <div class="skeleton-line skeleton-meta-line"></div>
      </div>
      <div class="skeleton-actions">
        <div class="skeleton-button"></div>
        <div class="skeleton-button"></div>
        <div class="skeleton-button"></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SkeletonLoader',
  props: {
    count: {
      type: Number,
      default: 3
    }
  }
}
</script>

<style scoped>
.skeleton-container {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.skeleton-item {
  background: #0f0f0f;
  border-radius: 16px;
  padding: 24px;
  border: 1px solid #1a1a1a;
  animation: pulse 1.5s ease-in-out infinite;
}

@keyframes pulse {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: 0.6;
  }
}

.skeleton-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 16px;
  gap: 16px;
}

.skeleton-badges {
  display: flex;
  gap: 8px;
}

.skeleton-line {
  background: linear-gradient(90deg, #1a1a1a 25%, #2a2a2a 50%, #1a1a1a 75%);
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
  border-radius: 4px;
  height: 16px;
}

@keyframes shimmer {
  0% {
    background-position: -200% 0;
  }
  100% {
    background-position: 200% 0;
  }
}

.skeleton-title {
  width: 60%;
  height: 24px;
}

.skeleton-description {
  width: 100%;
  margin-bottom: 8px;
}

.skeleton-description.short {
  width: 70%;
}

.skeleton-badge {
  width: 60px;
  height: 24px;
  background: linear-gradient(90deg, #1a1a1a 25%, #2a2a2a 50%, #1a1a1a 75%);
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
  border-radius: 12px;
}

.skeleton-meta {
  display: flex;
  justify-content: space-between;
  margin-top: 16px;
  padding-top: 16px;
  border-top: 1px solid #1a1a1a;
}

.skeleton-meta-line {
  width: 120px;
  height: 12px;
}

.skeleton-actions {
  display: flex;
  gap: 12px;
  margin-top: 20px;
}

.skeleton-button {
  width: 100px;
  height: 36px;
  background: linear-gradient(90deg, #1a1a1a 25%, #2a2a2a 50%, #1a1a1a 75%);
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
  border-radius: 8px;
}

@media (max-width: 768px) {
  .skeleton-item {
    padding: 20px;
  }
  
  .skeleton-actions {
    flex-direction: column;
  }
  
  .skeleton-button {
    width: 100%;
  }
}
</style>

