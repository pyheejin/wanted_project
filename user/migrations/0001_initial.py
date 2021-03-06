# Generated by Django 3.0.6 on 2020-06-17 05:06

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
                ('start_year', models.CharField(max_length=30, null=True)),
                ('start_month', models.CharField(max_length=30, null=True)),
                ('end_year', models.CharField(max_length=30, null=True)),
                ('end_month', models.CharField(max_length=30, null=True)),
                ('is_working', models.BooleanField(default=0)),
                ('company', models.CharField(max_length=100, null=True)),
                ('position', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'careers',
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
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('contact', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=500, null=True)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=0)),
                ('is_matchup', models.BooleanField(default=0)),
                ('image_url', models.URLField(max_length=2000, null=True)),
                ('title', models.CharField(max_length=150, null=True)),
                ('income', models.IntegerField(default=0)),
                ('total_work', models.IntegerField(default=0, null=True)),
                ('is_job_category', models.BooleanField(default=0)),
                ('job_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.Job_category')),
                ('matchup_career', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Matchup_career')),
            ],
            options={
                'db_table': 'resumes',
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
                ('image_url', models.URLField(default='https://s3.ap-northeast-2.amazonaws.com/wanted-public/profile_default.png', max_length=2000)),
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
                'db_table': 'securities',
            },
        ),
        migrations.CreateModel(
            name='Resume_role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Resume')),
                ('role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.Role')),
            ],
            options={
                'db_table': 'resume_roles',
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
        migrations.AddField(
            model_name='resume',
            name='resume_resume_role',
            field=models.ManyToManyField(related_name='resume_resume_role', through='user.Resume_role', to='company.Role'),
        ),
        migrations.AddField(
            model_name='resume',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.User'),
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_year', models.CharField(max_length=30, null=True)),
                ('start_month', models.CharField(max_length=30, null=True)),
                ('end_year', models.CharField(max_length=30, null=True)),
                ('end_month', models.CharField(max_length=30, null=True)),
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
                ('resume', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Resume')),
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
                ('resume', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Resume')),
            ],
            options={
                'db_table': 'matchup_jobs',
            },
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
        migrations.CreateModel(
            name='Exception',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.Company')),
                ('resume', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Resume')),
            ],
            options={
                'db_table': 'exceptions',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_year', models.CharField(max_length=30, null=True)),
                ('start_month', models.CharField(max_length=30, null=True)),
                ('end_year', models.CharField(max_length=30, null=True)),
                ('end_month', models.CharField(max_length=30, null=True)),
                ('school', models.CharField(max_length=100, null=True)),
                ('is_working', models.BooleanField(default=0)),
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
                ('date_year', models.CharField(max_length=30, null=True)),
                ('date_month', models.CharField(max_length=30, null=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('content', models.CharField(max_length=200, null=True)),
                ('resume', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Resume')),
            ],
            options={
                'db_table': 'awards',
            },
        ),
    ]
