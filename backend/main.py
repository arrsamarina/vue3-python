from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from datetime import datetime
import json
import os
from models import Task, TaskUpdate

app = FastAPI(title="Task Manager API", version="1.0.0")

# настройка cors для работы с фронтендом
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

TASKS_FILE = "tasks.json"

def load_tasks() -> List[dict]:
    """Загрузить задачи из файла"""
    # загрузка задач из json файла, возвращает пустой список при ошибке
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    return []

def save_tasks(tasks: List[dict]):
    """Сохранить задачи в файл"""
    # сохранение задач в json файл с форматированием
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

def get_next_id(tasks: List[dict]) -> int:
    """Получить следующий ID"""
    # генерация следующего id на основе максимального существующего
    if not tasks:
        return 1
    return max(task.get("id", 0) for task in tasks) + 1

@app.get("/")
async def root():
    return {"message": "Task Manager API", "version": "1.0.0"}

@app.get("/api/tasks", response_model=List[Task])
async def get_tasks():
    """Получить все задачи"""
    tasks = load_tasks()
    return tasks

@app.get("/api/tasks/{id}", response_model=Task)
async def get_task(id: int):
    """Получить задачу по ID"""
    tasks = load_tasks()
    task = next((t for t in tasks if t.get("id") == id), None)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.post("/api/tasks", response_model=Task)
async def create_task(task: Task):
    """Создать новую задачу"""
    tasks = load_tasks()
    new_id = get_next_id(tasks)
    task_dict = task.dict()
    task_dict["id"] = new_id
    # добавление временной метки создания задачи
    task_dict["created_at"] = datetime.now().isoformat()
    tasks.append(task_dict)
    save_tasks(tasks)
    return task_dict

@app.put("/api/tasks/{id}", response_model=Task)
async def update_task(id: int, task_update: TaskUpdate):
    """Обновить задачу"""
    tasks = load_tasks()
    # поиск индекса задачи по id
    task_index = next((i for i, t in enumerate(tasks) if t.get("id") == id), None)
    if task_index is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    task = tasks[task_index]
    # обновление только переданных полей
    update_data = task_update.dict(exclude_unset=True)
    task.update(update_data)
    save_tasks(tasks)
    return task

@app.delete("/api/tasks/{id}")
async def delete_task(id: int):
    """Удалить задачу"""
    tasks = load_tasks()
    task_index = next((i for i, t in enumerate(tasks) if t.get("id") == id), None)
    if task_index is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    deleted_task = tasks.pop(task_index)
    save_tasks(tasks)
    return {"message": "Task deleted", "task": deleted_task}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

