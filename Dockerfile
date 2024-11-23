# System Image
FROM python:3.13.0-slim

# Installing updates and necessary system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/*.bin

# Installing the working directory
WORKDIR /app/src

# Copying the dependency files
COPY requirements.txt requirements-dev.txt ./

# Installing dependencies
ARG DEV_ENV=false
RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && [ "$DEV_ENV" = "true" ] && pip install -r requirements-dev.txt || true \
    && rm -rf /root/.cache/pip

# Copying all project files
COPY . .

# Setting environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DJANGO_SETTINGS_MODULE=trello.settings

# The default startup command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
