# Generated by Django 4.0.1 on 2022-08-25 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_passwordanswer_user_passwordquestion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='passwordAnswer',
        ),
        migrations.RemoveField(
            model_name='user',
            name='passwordQuestion',
        ),
    ]
