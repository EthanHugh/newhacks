# Generated by Django 3.2.9 on 2021-11-06 18:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('assignment_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('course', models.CharField(max_length=30)),
                ('assignment_name', models.CharField(max_length=30)),
                ('date', models.IntegerField()),
                ('month', models.IntegerField()),
                ('weight', models.FloatField()),
                ('content', models.TextField()),
                ('submission_link', models.TextField()),
                ('reference_link', models.TextField()),
            ],
        ),
    ]
