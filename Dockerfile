# Используйте официальный образ Python
FROM python:3.11-slim

# Установите рабочий каталог в контейнере
WORKDIR /app

# Скопируйте файлы зависимостей в рабочую директорию
COPY requirements.txt .

# Установите зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Скопируйте все файлы проекта в рабочую директорию
COPY . .

# Задайте команду для запуска приложения
CMD ["python", "main_weather_tg_bot.py"]
