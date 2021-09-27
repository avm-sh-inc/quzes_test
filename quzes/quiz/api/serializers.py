from django.contrib.auth import get_user_model
from rest_framework import serializers

from quzes.quiz.models import Quize


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quize
        fields = '__all__'
