// базовый url api (используется nginx proxy в docker или переменная окружения)
const API_BASE_URL = import.meta.env.VITE_API_URL || '/api'

export const taskService = {
  async getAllTasks() {
    const response = await fetch(`${API_BASE_URL}/tasks`)
    if (!response.ok) {
      throw new Error('Failed to fetch tasks')
    }
    return await response.json()
  },

  async getTaskById(id) {
    const response = await fetch(`${API_BASE_URL}/tasks/${id}`)
    if (!response.ok) {
      throw new Error('Failed to fetch task')
    }
    return await response.json()
  },

  async createTask(task) {
    const response = await fetch(`${API_BASE_URL}/tasks`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(task)
    })
    if (!response.ok) {
      throw new Error('Failed to create task')
    }
    return await response.json()
  },

  async updateTask(id, task) {
    const response = await fetch(`${API_BASE_URL}/tasks/${id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(task)
    })
    if (!response.ok) {
      throw new Error('Failed to update task')
    }
    return await response.json()
  },

  async deleteTask(id) {
    const response = await fetch(`${API_BASE_URL}/tasks/${id}`, {
      method: 'DELETE'
    })
    if (!response.ok) {
      throw new Error('Failed to delete task')
    }
    return await response.json()
  }
}

