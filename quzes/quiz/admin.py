from django.contrib import admin

# Register your models here.
from quzes.quiz.models import Quize


@admin.register(Quize)
class QuizeAdmin(admin.ModelAdmin):
    pass
