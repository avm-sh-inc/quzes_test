from uuid import uuid4

from django.contrib.postgres.fields import JSONField
from django.db import models

from quzes.questions.models import Question


class Quize(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    title = models.CharField(max_length=120)
    pic_title = models.FileField()
    description = models.TextField()
    type = models.CharField(max_length=120)
    creator = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=False)
    questions = models.ManyToManyField(Question)
    rules = JSONField()


    class Meta:
        db_table = 'quize'
