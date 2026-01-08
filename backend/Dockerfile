FROM python:3.11-slim

WORKDIR /app

# установка зависимостей python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# копирование исходного кода
COPY . .

EXPOSE 8000

# запуск fastapi сервера
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

