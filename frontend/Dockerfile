# этап сборки
FROM node:18-alpine as build

WORKDIR /app

# копирование package файлов для установки зависимостей
COPY package*.json ./

# установка зависимостей
RUN npm install

# копирование исходного кода
COPY . .

# сборка приложения
RUN npm run build

# этап продакшн
FROM nginx:alpine

# копирование собранного приложения в nginx
COPY --from=build /app/dist /usr/share/nginx/html

# копирование конфигурации nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

