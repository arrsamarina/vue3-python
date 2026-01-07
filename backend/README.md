# Task Manager Backend

FastAPI сервер для управления задачами.

## Разработка

```bash
pip install -r requirements.txt
python main.py
```

Сервер будет доступен на http://localhost:8000

API документация: http://localhost:8000/docs

## API Endpoints

- `GET /api/tasks` - Получить все задачи
- `GET /api/tasks/{id}` - Получить задачу по ID
- `POST /api/tasks` - Создать новую задачу
- `PUT /api/tasks/{id}` - Обновить задачу
- `DELETE /api/tasks/{id}` - Удалить задачу

## Хранение данных

Данные хранятся в файле `tasks.json` в корне проекта.

