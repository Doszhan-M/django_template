from logging import getLogger

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission

from core.config import setup


logger = getLogger("django")


class StartUpManager:

    @classmethod
    def startup_actions(cls) -> None:
        logger.info("Startup check accounts")
        cls.check_admin_user()

    @staticmethod
    def check_admin_user() -> None:
        if get_user_model().objects.filter(email=setup.ADMIN_EMAIL).exists():
            return
        get_user_model().objects.create_superuser(
            phone=setup.ADMIN_PHONE,
            email=setup.ADMIN_EMAIL,
            password=setup.ADMIN_PASS,
        )
        logger.info("Created superuser")
