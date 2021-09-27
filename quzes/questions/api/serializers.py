from rest_framework import serializers

from quzes.questions.models import Question


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
