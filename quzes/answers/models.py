from uuid import uuid4

from django.db import models


class Answers(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    quiz = models.ForeignKey('quiz.Quiz', on_delete=models.SET_NULL, blank=False, null=True)
    question = models.ForeignKey('questions.Question', on_delete=models.PROTECT, blank=False, null=False)
    interviewee = models.ForeignKey('users.User', on_delete=models.PROTECT, blank=False, null=False)
    value = models.CharField(max_length=100)

    class Meta:
        db_table = 'answers'
        ordering = ['quiz']
        indexes = [
            models.Index(fields=['quiz'], name='quiz_idx'),
            models.Index(fields=['value'], name='value_idx'),
            models.Index(fields=['question'], name='question_idx'),
        ]
        unique_together = [['quiz', 'question']]
