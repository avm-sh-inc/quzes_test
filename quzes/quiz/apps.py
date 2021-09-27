from django.apps import AppConfig


class QuizConfig(AppConfig):
    name = 'quzes.quiz'

    def ready(self):
        try:
            import quzes.quiz.signals  # noqa F401

        except ImportError:
            pass
