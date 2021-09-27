from django.contrib import admin

# Register your models here.
from quzes.quiz.models import Quiz


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    pass
