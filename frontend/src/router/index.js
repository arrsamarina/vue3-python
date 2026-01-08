import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Tasks from '../views/Tasks.vue'
import TaskNew from '../views/TaskNew.vue'
import TaskEdit from '../views/TaskEdit.vue'
import NotFound from '../views/NotFound.vue'

// определение маршрутов приложения
const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/tasks',
    name: 'tasks',
    component: Tasks
  },
  {
    path: '/tasks/new',
    name: 'task-new',
    component: TaskNew
  },
  {
    path: '/tasks/:id/edit',
    name: 'task-edit',
    component: TaskEdit,
    props: true
  },
  {
    // catch-all маршрут для 404 страницы
    path: '/:pathMatch(.*)*',
    name: 'not-found',
    component: NotFound
  }
]

// создание роутера с history mode
const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router

