# Generated by Django 4.0.1 on 2022-08-25 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0002_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='filePath',
        ),
    ]