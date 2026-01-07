from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import json
import os

app = FastAPI(title="Task Manager API", version="1.0.0")

# CORS middleware для работы с фронтендом
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

TASKS_FILE = "tasks.json"

# Модели данных
class Task(BaseModel):
    id: Optional[int] = None
    title: str
    description: str
    priority: str  # low, medium, high
    category: str  # work, personal, development
    important: bool
    completed: bool = False
    created_at: Optional[str] = None

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    category: Optional[str] = None
    important: Optional[bool] = None
    completed: Optional[bool] = None

# Функции для работы с файлом
def load_tasks() -> List[dict]:
    """Загрузить задачи из файла"""
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    return []

def save_tasks(tasks: List[dict]):
    """Сохранить задачи в файл"""
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

def get_next_id(tasks: List[dict]) -> int:
    """Получить следующий ID"""
    if not tasks:
        return 1
    return max(task.get("id", 0) for task in tasks) + 1

# API endpoints
@app.get("/")
async def root():
    return {"message": "Task Manager API", "version": "1.0.0"}

@app.get("/api/tasks", response_model=List[Task])
async def get_tasks():
    """Получить все задачи"""
    tasks = load_tasks()
    return tasks

@app.get("/api/tasks/{task_id}", response_model=Task)
async def get_task(task_id: int):
    """Получить задачу по ID"""
    tasks = load_tasks()
    task = next((t for t in tasks if t.get("id") == task_id), None)
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
    task_dict["created_at"] = datetime.now().isoformat()
    tasks.append(task_dict)
    save_tasks(tasks)
    return task_dict

@app.put("/api/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task_update: TaskUpdate):
    """Обновить задачу"""
    tasks = load_tasks()
    task_index = next((i for i, t in enumerate(tasks) if t.get("id") == task_id), None)
    if task_index is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    task = tasks[task_index]
    update_data = task_update.dict(exclude_unset=True)
    task.update(update_data)
    save_tasks(tasks)
    return task

@app.delete("/api/tasks/{task_id}")
async def delete_task(task_id: int):
    """Удалить задачу"""
    tasks = load_tasks()
    task_index = next((i for i, t in enumerate(tasks) if t.get("id") == task_id), None)
    if task_index is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    deleted_task = tasks.pop(task_index)
    save_tasks(tasks)
    return {"message": "Task deleted", "task": deleted_task}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

