# Generated by Django 3.0 on 2023-11-11 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Mytodoapp',
            new_name='Task',
        ),
    ]
