# Generated by Django 3.2.9 on 2022-01-25 01:08

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
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Old_Assignment',
            fields=[
                ('assignment_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('course', models.CharField(max_length=30)),
                ('assignment_name', models.CharField(max_length=30)),
                ('date', models.DateField()),
            ],
        ),
    ]
