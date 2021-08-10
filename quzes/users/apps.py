import logging

from django.apps import AppConfig
from django.conf import settings
from django.contrib.auth.apps import AuthConfig
from django.db.models.signals import post_migrate
from django.utils.translation import gettext_lazy as _




class UsersConfig(AppConfig):
    name = "quzes.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import quzes.users.signals  # noqa F401

        except ImportError:
            pass
