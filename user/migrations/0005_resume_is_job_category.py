# Generated by Django 3.0.6 on 2020-06-10 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20200609_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='is_job_category',
            field=models.BooleanField(default=0),
        ),
    ]
