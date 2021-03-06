# Generated by Django 2.2.10 on 2021-09-27 17:52

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quize',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=120)),
                ('pic_title', models.FileField(upload_to='')),
                ('description', models.TextField()),
                ('type', models.CharField(max_length=120)),
                ('rules', django.contrib.postgres.fields.jsonb.JSONField()),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('questions', models.ManyToManyField(to='questions.Question')),
            ],
            options={
                'db_table': 'quize',
            },
        ),
    ]
