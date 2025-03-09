import os
from pathlib import Path

from . import logger
from .config import setup


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = setup.SECRET_KEY

DEBUG = setup.DEBUG

ALLOWED_HOSTS = setup.ALLOWED_HOSTS.split(" ")

CSRF_TRUSTED_ORIGINS = setup.CSRF_AND_CORS_ALLOWED_ORIGINS.split(" ")
CORS_ALLOWED_ORIGINS = setup.CSRF_AND_CORS_ALLOWED_ORIGINS.split(" ")
CORS_EXPOSE_HEADERS = ["Content-Type", "X-CSRFToken"]
CORS_ALLOW_CREDENTIALS = True

# Application definition

INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "whitenoise",
    "corsheaders",
    "rest_framework",
    "sitemap_generate",
    "django.contrib.sitemaps",
    "accounts",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # 'querycount.middleware.QueryCountMiddleware',
]

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
    ),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
}


ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": setup.POSTGRES_DBNAME,
        "USER": setup.POSTGRES_USER,
        "PASSWORD": setup.POSTGRES_PASSWORD,
        "HOST": setup.POSTGRES_HOST,
        "PORT": setup.POSTGRES_PORT,
    }
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": setup.BACKEND_CACHE,
        "OPTIONS": {},
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTH_USER_MODEL = "accounts.User"
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_COOKIE_AGE = 60 * 60 * 24 * 30
CSRF_COOKIE_SAMESITE = "Strict"
SESSION_COOKIE_SAMESITE = "Strict"
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

DATA_UPLOAD_MAX_MEMORY_SIZE = 5242880
DATA_UPLOAD_MAX_NUMBER_FIELDS = 10000

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


STATIC_URL = "/backend_static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
WHITENOISE_AUTOREFRESH = False
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGGING = logger.config

JAZZMIN_SETTINGS = {
    "site_title": "Trust Finance Admin",
    "site_header": "Trust Finance",
    "site_brand": "TrustSoft",
    "welcome_sign": "Welcome to the Admin Panel!",
    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {
            "name": "Documentation",
            "url": "https://docs.trustfinance.com",
            "new_window": True,
        },
    ],
    "user_avatar": None,
    "custom_links": {
        "Finance": [  # Название группы (подзаголовка)
            {
                "name": "Users & Transactions",
                "url": "admin:accounts_user_changelist",
                "icon": "fas fa-users",
                "permissions": ["auth.view_user"],
            },
            {
                "name": "All Transactions",
                "url": "admin:transactions_transaction_changelist",
                "icon": "fas fa-money-bill-wave",
                "permissions": ["auth.view_transaction"],
            },
        ],
    },
}

JAZZMIN_UI_TWEAKS = {
    "theme": "darkly",
}
