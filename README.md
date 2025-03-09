# Django Template Project

This is a Django project template designed for fast and scalable development.  
It includes a pre-configured setup with Docker, PostgreSQL, Redis, and Django REST Framework.

## Features

- 🔥 Django 5.0 with REST API support (`djangorestframework`)
- 🗄️ PostgreSQL & Redis integration
- 🏗️ Custom user model with `email` authentication
- 🔐 Admin panel with `Jazzmin`
- 📦 Docker & Docker Compose support
- 🚀 Gunicorn for production
- ⚙️ Configuration via `.env` files
- 📜 Logging system with `colorlog`

## Installation

### 3 Build and run the project with Docker
```sh
docker network create trust-soft
docker volume create redis-trust-soft
docker volume create pgdata-trust-soft
docker-compose up -d --build
```

### Project Structure
```
.
├── README.md               # Project documentation
├── docker-compose.yml      # Docker services configuration
├── env/                    # Environment variables
│   ├── backend.env
│   ├── postgresql.env
├── backend/                # Django application
│   ├── app/                # Main Django app
│   │   ├── core/           # Main settings & configurations
│   │   ├── accounts/       # User management app
│   ├── dockerfile          # Backend Dockerfile
```

### Contributing
Feel free to contribute by creating issues or pull requests.
