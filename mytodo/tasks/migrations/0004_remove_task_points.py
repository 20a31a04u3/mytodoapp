# Generated by Django 3.0 on 2023-11-12 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_task_points'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='points',
        ),
    ]
