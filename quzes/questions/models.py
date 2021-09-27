from uuid import uuid4

from django.db import models


class Question(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    text = models.TextField()
    name = models.CharField(max_length=100, blank=False, null=True, default=None)
    type = models.CharField(max_length=100)
    required = models.BooleanField(default=False)
    archive = models.BooleanField(default=False)
    exception_date = models.DateField()
    replacement = models.ForeignKey('questions.Question', on_delete=models.SET_NULL, related_name='parent', null=True)
    offer_to_set = models.BooleanField(default=False)

    class Meta:
        db_table = 'questions'
