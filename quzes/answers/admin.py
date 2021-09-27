from django.contrib import admin

# Register your models here.
from quzes.answers.models import Answers


@admin.register(Answers)
class AnswersAdmin(admin.ModelAdmin):
    pass
