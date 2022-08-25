# Generated by Django 4.0.1 on 2022-08-25 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fileName', models.CharField(default='', max_length=200, null=True)),
                ('filePath', models.FileField(blank=True, null=True, upload_to='Uploaded Files/')),
                ('uploadTime', models.DateField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]
