from django.contrib.auth import get_user_model
from rest_framework import serializers

from quzes.quiz.models import Quiz


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'
