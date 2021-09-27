from django.apps import AppConfig


class FrontendConfig(AppConfig):
    name = 'frontend'

    def ready(self):
        try:
            import quzes.frontend.signals  # noqa F401

        except ImportError:
            pass
