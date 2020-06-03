# Generated by Django 3.0.6 on 2020-06-03 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_resume_deleted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='career',
        ),
        migrations.AddField(
            model_name='education',
            name='resume',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Resume'),
        ),
    ]
