from django.apps import AppConfig


class QuestionsConfig(AppConfig):
    name = 'questions'

    def ready(self):
        try:
            import quzes.questions.signals  # noqa F401

        except ImportError:
            pass
