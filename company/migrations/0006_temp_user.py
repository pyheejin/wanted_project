# Generated by Django 3.0.6 on 2020-06-16 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_temp'),
    ]

    operations = [
        migrations.AddField(
            model_name='temp',
            name='user',
            field=models.IntegerField(null=True),
        ),
    ]
