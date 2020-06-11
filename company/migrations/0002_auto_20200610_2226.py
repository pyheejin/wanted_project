# Generated by Django 3.0.6 on 2020-06-10 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200610_2226'),
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='position',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.Position'),
        ),
        migrations.AddField(
            model_name='bookmark',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.User'),
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.Country'),
        ),
        migrations.AddField(
            model_name='company',
            name='companies_like_matchup',
            field=models.ManyToManyField(related_name='companies_resumes', through='company.Like', to='user.Resume'),
        ),
        migrations.AddField(
            model_name='company',
            name='companies_matchup_items',
            field=models.ManyToManyField(related_name='companies_matchup_items', through='company.Company_matchup_item', to='company.Matchup_item'),
        ),
        migrations.AddField(
            model_name='company',
            name='companies_tag',
            field=models.ManyToManyField(related_name='companies_tag', through='company.Company_tag', to='company.Tag'),
        ),
        migrations.AddField(
            model_name='company',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.Employee'),
        ),
        migrations.AddField(
            model_name='company',
            name='foundation_year',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.Foundation_year'),
        ),
        migrations.AddField(
            model_name='company',
            name='industry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.Industry'),
        ),
        migrations.AddField(
            model_name='company',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.User'),
        ),
        migrations.AddField(
            model_name='company_matchup',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.Company'),
        ),
        migrations.AddField(
            model_name='company_matchup',
            name='resume',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Resume'),
        ),
        migrations.AddField(
            model_name='company_matchup_item',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.Company'),
        ),
        migrations.AddField(
            model_name='company_matchup_item',
            name='matchup_item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.Matchup_item'),
        ),
        migrations.AddField(
            model_name='company_tag',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.Company'),
        ),
        migrations.AddField(
            model_name='company_tag',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.Tag'),
        ),
        migrations.AddField(
            model_name='image',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.Company'),
        ),
        migrations.AddField(
            model_name='like',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.Company'),
        ),
        migrations.AddField(
            model_name='like',
            name='resume',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Resume'),
        ),
        migrations.AddField(
            model_name='network',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.Item'),
        ),
        migrations.AddField(
            model_name='position',
            name='bookmarks',
            field=models.ManyToManyField(through='company.Bookmark', to='user.User'),
        ),
        migrations.AddField(
            model_name='position',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.City'),
        ),
        migrations.AddField(
            model_name='position',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.Company'),
        ),
        migrations.AddField(
            model_name='position',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.Country'),
        ),
        migrations.AddField(
            model_name='position',
            name='position_items',
            field=models.ManyToManyField(related_name='position_items', through='company.Position_item', to='company.Item'),
        ),
        migrations.AddField(
            model_name='position',
            name='position_volunteers',
            field=models.ManyToManyField(related_name='position_volunteers', through='company.Volunteers', to='user.User'),
        ),
        migrations.AddField(
            model_name='position',
            name='position_workplaces',
            field=models.ManyToManyField(related_name='position_workplaces', through='company.Position_workplace', to='company.Workplace'),
        ),
        migrations.AddField(
            model_name='position',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.Role'),
        ),
        migrations.AddField(
            model_name='position',
            name='theme',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.Theme'),
        ),
        migrations.AddField(
            model_name='position',
            name='workplace',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.Workplace'),
        ),
        migrations.AddField(
            model_name='position_item',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.Company'),
        ),
        migrations.AddField(
            model_name='position_item',
            name='expiration',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.Expiration'),
        ),
        migrations.AddField(
            model_name='position_item',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.Item'),
        ),
        migrations.AddField(
            model_name='position_item',
            name='position',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.Position'),
        ),
        migrations.AddField(
            model_name='position_workplace',
            name='position',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.Position'),
        ),
        migrations.AddField(
            model_name='position_workplace',
            name='workplace',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.Workplace'),
        ),
        migrations.AddField(
            model_name='proposal',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.Company'),
        ),
        migrations.AddField(
            model_name='proposal',
            name='position',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.Position'),
        ),
        migrations.AddField(
            model_name='proposal',
            name='resume',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Resume'),
        ),
        migrations.AddField(
            model_name='reading',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.Company'),
        ),
        migrations.AddField(
            model_name='reading',
            name='resume',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Resume'),
        ),
        migrations.AddField(
            model_name='role',
            name='job_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.Job_category'),
        ),
        migrations.AddField(
            model_name='tag',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.Category'),
        ),
        migrations.AddField(
            model_name='volunteers',
            name='resume',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Resume'),
        ),
        migrations.AddField(
            model_name='volunteers',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='volunteers', to='user.User'),
        ),
    ]
