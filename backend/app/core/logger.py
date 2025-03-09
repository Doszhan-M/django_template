from .config import setup


config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": " {asctime} - {levelname} - {message}",
            "datefmt": "%d-%m-%Y %H:%M:%S",
            "style": "{",
        },
        "color": {
            "()": "colorlog.ColoredFormatter",
            "format": "%(asctime)s - %(log_color)s%(levelname)-1s%(reset)s - %(yellow)s%(message)s",
            "datefmt": "%d-%m-%Y %H:%M:%S",
            "log_colors": {
                "DEBUG": "bold_black",
                "INFO": "green",
                "WARNING": "light_yellow",
                "ERROR": "bold_red",
                "CRITICAL": "red,bg_white",
            },
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "color",
        },
        "sql_console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": True,
        },
        "gunicorn": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": True,
        },
        "celery": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": True,
        },
        # 'django.db.backends': { # закомментировать для выключения вывода sql запросов
        #     'level': 'DEBUG',
        #     'handlers': ["sql_console"],
        #     "propagate": False,
        # },
    },
}
