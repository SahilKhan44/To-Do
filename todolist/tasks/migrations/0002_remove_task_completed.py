# Generated by Django 5.0.7 on 2024-08-01 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='completed',
        ),
    ]
