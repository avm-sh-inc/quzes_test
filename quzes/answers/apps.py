from django.apps import AppConfig




class AnswersConfig(AppConfig):
    name = 'quzes.answers'


    def ready(self) -> None:
        try:
            from . import signals
        except ImportError:
            pass
