# Using the official Python image
FROM python:3.10-slim

# Installing dependencies
RUN pip install --upgrade pip
RUN pip install django
RUN pip install django-allauth

# Creating a working directory
WORKDIR /app

# Copy the project to the container
COPY . /app

# Opening port 8000 to access Django
EXPOSE 8000

# The command to start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
