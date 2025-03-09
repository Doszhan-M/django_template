from pydantic_settings import BaseSettings


class Setup(BaseSettings):
    DEPLOY: bool
    DEBUG: bool
    SECRET_KEY: str
    ALLOWED_HOSTS: str
    CSRF_AND_CORS_ALLOWED_ORIGINS: str

    ADMIN_EMAIL: str
    ADMIN_PASS: str
    ADMIN_PHONE: str = ""

    BACKEND_CACHE: str

    POSTGRES_DBNAME: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    
    
setup = Setup()
