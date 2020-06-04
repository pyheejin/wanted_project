# Generated by Django 3.0.6 on 2020-06-04 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(null=True)),
                ('end', models.DateTimeField(null=True)),
                ('is_working', models.BooleanField(default=0)),
                ('company', models.CharField(max_length=100, null=True)),
                ('position', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'careers',
            },
        ),
        migrations.CreateModel(
            name='Exception',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.Company')),
            ],
            options={
                'db_table': 'exceptions',
            },
        ),
        migrations.CreateModel(
            name='Job_text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_working', models.CharField(max_length=50)),
                ('text', models.CharField(max_length=50)),
                ('agreement', models.BooleanField(default=0)),
            ],
            options={
                'db_table': 'job_texts',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'languages',
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'levels',
            },
        ),
        migrations.CreateModel(
            name='Linguistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'linguistics',
            },
        ),
        migrations.CreateModel(
            name='Matchup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income', models.IntegerField(default=0)),
                ('school', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(blank=True)),
                ('companies_exception', models.ManyToManyField(related_name='companies_exception', through='user.Exception', to='company.Company')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.Country')),
            ],
            options={
                'db_table': 'matchup',
            },
        ),
        migrations.CreateModel(
            name='Matchup_career',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'matchup_careers',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=500)),
                ('password', models.CharField(max_length=500)),
                ('agreement', models.BooleanField(default=0)),
                ('contact', models.CharField(max_length=50, null=True)),
                ('image_url', models.URLField(max_length=2000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('fail_count', models.IntegerField(default=0)),
                ('deleted', models.BooleanField(default=0)),
                ('job_position', models.CharField(max_length=100, null=True)),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.Country')),
                ('user_bookmark', models.ManyToManyField(related_name='user_bookmark', through='company.Bookmark', to='company.Position')),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Work_information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start', models.DateField(null=True)),
                ('end', models.DateField(null=True)),
                ('is_working', models.BooleanField(default=0)),
                ('matchup', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Matchup')),
            ],
            options={
                'db_table': 'work_informations',
            },
        ),
        migrations.CreateModel(
            name='Want',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.Company')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.User')),
            ],
            options={
                'db_table': 'wants',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, null=True)),
                ('score', models.CharField(max_length=150, null=True)),
                ('date', models.DateField(null=True)),
                ('language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Language')),
            ],
            options={
                'db_table': 'tests',
            },
        ),
        migrations.CreateModel(
            name='Security',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_ip', models.CharField(max_length=100)),
                ('browser', models.CharField(max_length=1000)),
                ('date', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.User')),
            ],
            options={
                'db_table': 'security',
            },
        ),
        migrations.CreateModel(
            name='Resume_file',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume_file', models.FilePathField(path='/user/resumes')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.User')),
            ],
            options={
                'db_table': 'resume_files',
            },
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, null=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('contact', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=500, null=True)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=0)),
                ('is_matchup', models.BooleanField(default=0)),
                ('image_url', models.URLField(max_length=2000, null=True)),
                ('deleted', models.BooleanField(default=0)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.User')),
            ],
            options={
                'db_table': 'resumes',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(null=True)),
                ('end', models.DateTimeField(null=True)),
                ('title', models.CharField(max_length=300, null=True)),
                ('content', models.CharField(max_length=300, null=True)),
                ('career', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Career')),
            ],
            options={
                'db_table': 'results',
            },
        ),
        migrations.CreateModel(
            name='Matchup_skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=50, null=True)),
                ('matchup', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Matchup')),
            ],
            options={
                'db_table': 'matchup_skills',
            },
        ),
        migrations.CreateModel(
            name='Matchup_job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_text', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Job_text')),
                ('matchup', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Matchup')),
            ],
            options={
                'db_table': 'matchup_jobs',
            },
        ),
        migrations.AddField(
            model_name='matchup',
            name='matchup_career',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Matchup_career'),
        ),
        migrations.AddField(
            model_name='matchup',
            name='resume',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Resume'),
        ),
        migrations.AddField(
            model_name='matchup',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.Role'),
        ),
        migrations.AddField(
            model_name='matchup',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.User'),
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=2000, null=True)),
                ('resume', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Resume')),
            ],
            options={
                'db_table': 'links',
            },
        ),
        migrations.AddField(
            model_name='language',
            name='level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Level'),
        ),
        migrations.AddField(
            model_name='language',
            name='linguistic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Linguistic'),
        ),
        migrations.AddField(
            model_name='language',
            name='resume',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Resume'),
        ),
        migrations.AddField(
            model_name='exception',
            name='matchup',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Matchup'),
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(null=True)),
                ('end', models.DateTimeField(null=True)),
                ('is_working', models.BooleanField(default=0)),
                ('school', models.CharField(max_length=100, null=True)),
                ('specialism', models.CharField(max_length=100, null=True)),
                ('subject', models.CharField(max_length=200, null=True)),
                ('resume', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Resume')),
            ],
            options={
                'db_table': 'educations',
            },
        ),
        migrations.AddField(
            model_name='career',
            name='resume',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Resume'),
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(null=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('content', models.CharField(max_length=200, null=True)),
                ('resume', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Resume')),
            ],
            options={
                'db_table': 'awards',
            },
        ),
    ]
