from pydantic import BaseModel
from typing import Optional

class Task(BaseModel):
    # модель задачи для создания и получения
    id: Optional[int] = None
    title: str
    description: str
    priority: str  # low, medium, high
    category: str  # work, personal, development
    important: bool
    completed: bool = False
    created_at: Optional[str] = None

class TaskUpdate(BaseModel):
    # модель для частичного обновления задачи (все поля опциональны)
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    category: Optional[str] = None
    important: Optional[bool] = None
    completed: Optional[bool] = None

