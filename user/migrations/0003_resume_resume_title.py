# Generated by Django 3.0.6 on 2020-06-01 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200601_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='resume_title',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
