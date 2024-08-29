# Используем официальный образ Python
FROM python:3.10-slim

# Устанавливаем зависимости
RUN pip install --upgrade pip
RUN pip install django

# Создаем рабочую директорию
WORKDIR /app

# Копируем проект в контейнер
COPY . /app

# Открываем порт 8000 для доступа к Django
EXPOSE 8000

# Команда для запуска сервера разработки Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
