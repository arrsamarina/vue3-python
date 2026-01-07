# Task Manager - Vue 3 + Python FastAPI

## 📋 Титульная часть

**Автор:** Арина Самарина  
**Группа:** Р3468  
**Дата:** 2024  
**Название работы:** Разработка SPA-приложения «Менеджер задач» на Vue 3 с сервером на Python

## 🎯 Цель работы

Освоить фундаментальные возможности Vue 3:
- Привязка данных, события, computed, watch
- Формы и модификаторы ввода
- Условный рендеринг
- Вывод массивов, сортировка, фильтрация
- Компоненты, props, события, слоты
- Маршрутизация Vue Router
- Работа с refs и жизненным циклом

Научиться взаимодействовать с сервером (REST API), освоить базовую серверную разработку на Python (FastAPI), освоить контейнеризацию приложения (Docker).

## 🚀 Реализованный функционал

### Клиентская часть (Vue 3)

#### Компоненты:
- **AppHeader.vue** - Верхнее меню навигации
- **AppFooter.vue** - Нижняя панель
- **TaskList.vue** - Список задач с фильтрацией и сортировкой
- **TaskItem.vue** - Отображение одной задачи с событиями
- **TaskForm.vue** - Форма создания/редактирования задачи
- **LayoutCard.vue** - Компонент с слотами (обычный, именованный, с ограниченной областью видимости)

#### Computed и Watch:
- `sortedTasks` - вычисляемое свойство для сортировки задач
- `filteredTasks` - вычисляемое свойство для фильтрации задач
- Watch на изменения фильтров и сортировки

#### Слоты:
- **Обычный слот** - в LayoutCard.vue для основного контента
- **Именованный слот** - `header` и `footer` в LayoutCard.vue
- **Слот с ограниченной областью видимости** - передача данных задачи в TaskItem

#### Маршруты:
- `/` - Главная страница (Dashboard)
- `/tasks` - Список задач
- `/tasks/new` - Создание новой задачи
- `/tasks/:id/edit` - Редактирование задачи
- `*` - Страница 404

#### Программная навигация:
- Использование `router.push()` для перехода между страницами
- Использование `router.params` для получения ID задачи

### Серверная часть (Python FastAPI)

#### CRUD методы:
- `GET /api/tasks` - Получить все задачи
- `GET /api/tasks/{id}` - Получить задачу по ID
- `POST /api/tasks` - Создать новую задачу
- `PUT /api/tasks/{id}` - Обновить задачу
- `DELETE /api/tasks/{id}` - Удалить задачу

#### Хранение данных:
- Данные хранятся в файле `tasks.json` в корне backend проекта
- При каждом запросе данные записываются в файл

## 📸 Скриншоты интерфейса

_Примечание: Для получения скриншотов запустите приложение и сделайте снимки экрана_

1. Главная страница - Dashboard с приветствием и кнопкой перехода к задачам
2. Список задач - Отображение всех задач с фильтрацией и сортировкой
3. Фильтрация/сортировка - Работа фильтров по статусу и сортировки
4. Форма создания - Форма с валидацией для создания новой задачи
5. Форма редактирования - Форма с предзаполненными данными для редактирования
6. Страница 404 - Обработка несуществующих маршрутов

## 💻 Пример кода

### Компонент TaskItem с событиями:

```vue
<TaskItem
  v-for="task in sortedTasks"
  :key="task.id"
  :task="task"
  @delete="removeTask"
  @toggle="toggleTaskStatus"
  @edit="editTask"
/>
```

### Computed свойство для сортировки:

```javascript
const sortedTasks = computed(() => {
  const tasks = [...filteredTasks.value];
  if (sortBy.value === 'date') {
    return tasks.sort((a, b) => new Date(b.created_at) - new Date(a.created_at));
  } else if (sortBy.value === 'alphabet') {
    return tasks.sort((a, b) => a.title.localeCompare(b.title));
  }
  return tasks;
});
```

### Использование слотов:

```vue
<LayoutCard>
  <template #header>
    <h2>Заголовок</h2>
  </template>
  
  <template #default="{ data }">
    <p>{{ data }}</p>
  </template>
  
  <template #footer>
    <button>Действие</button>
  </template>
</LayoutCard>
```

## 📊 Пример данных (tasks.json)

```json
[
  {
    "id": 1,
    "title": "Создать Vue-компонент",
    "description": "Разработать компонент TaskItem",
    "completed": false,
    "priority": "high",
    "category": "development",
    "important": true,
    "created_at": "2024-01-15T10:00:00"
  },
  {
    "id": 2,
    "title": "Настроить маршрутизацию",
    "description": "Добавить Vue Router",
    "completed": true,
    "priority": "medium",
    "category": "development",
    "important": false,
    "created_at": "2024-01-14T15:30:00"
  }
]
```

## 🐳 Инструкция по запуску (Docker)

### Требования:
- Docker
- Docker Compose

### Запуск:

1. Клонируйте репозиторий:
```bash
git clone <repository-url>
cd vue3
```

2. Соберите и запустите контейнеры:
```bash
docker compose build
docker compose up
```

3. Откройте браузер:
- Frontend: http://localhost:80
- Backend API: http://localhost:8000
- API документация: http://localhost:8000/docs

### Остановка:
```bash
docker compose down
```

## 📝 Выводы

В ходе выполнения задания было изучено:

1. **Vue 3 структуры и синтаксис** - освоены основные директивы, реактивность, computed свойства, watch
2. **Компонентный подход** - создание переиспользуемых компонентов с props и событиями
3. **Маршрутизация** - настройка Vue Router, работа с динамическими маршрутами, программная навигация
4. **Работа с формами** - использование v-model, модификаторов, валидация
5. **API-взаимодействие** - работа с REST API через fetch, обработка ошибок
6. **Работа с Docker** - создание Dockerfile для фронтенда и бэкенда, настройка docker-compose
7. **Структурирование SPA-проекта** - организация кода, разделение на компоненты и страницы
8. **Слоты** - использование обычных, именованных и слотов с ограниченной областью видимости
9. **Серверная разработка на Python** - создание REST API с FastAPI, работа с JSON файлами

## 🔗 Ссылка на репозиторий

[Вставьте ссылку на ваш репозиторий здесь]

## 📁 Структура проекта

```
/
├── frontend/              # Vue 3 клиентское приложение
│   ├── src/
│   │   ├── components/    # Vue компоненты
│   │   │   ├── AppHeader.vue
│   │   │   ├── AppFooter.vue
│   │   │   ├── TaskList.vue
│   │   │   ├── TaskItem.vue
│   │   │   ├── TaskForm.vue
│   │   │   └── LayoutCard.vue (с слотами)
│   │   ├── views/         # Страницы
│   │   │   ├── Home.vue
│   │   │   ├── Tasks.vue
│   │   │   ├── TaskNew.vue
│   │   │   ├── TaskEdit.vue
│   │   │   └── NotFound.vue
│   │   ├── router/        # Маршрутизация
│   │   ├── services/      # API сервисы
│   │   └── App.vue
│   ├── public/
│   ├── package.json
│   ├── vite.config.js
│   ├── Dockerfile
│   └── nginx.conf
│
├── backend/               # FastAPI сервер
│   ├── main.py           # Основной файл сервера
│   ├── requirements.txt
│   ├── tasks.json        # Хранилище данных
│   └── Dockerfile
│
├── docker-compose.yml    # Оркестрация контейнеров
└── README.md            # Документация проекта
```

## 🛠️ Технологии

### Frontend:
- Vue 3 (Composition API)
- Vue Router 4
- Vite
- Nginx (для продакшн)

### Backend:
- Python 3.11
- FastAPI
- Uvicorn

### DevOps:
- Docker
- Docker Compose

