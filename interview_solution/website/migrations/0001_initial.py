# Generated by Django 3.0.7 on 2020-10-04 09:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name='pk')),
                ('userID', models.CharField(max_length=10, unique=True, verbose_name='아이디')),
                ('username', models.CharField(blank=True, max_length=10, null=True, verbose_name='유저이름')),
                ('password', models.CharField(max_length=20, verbose_name='비밀번호')),
                ('phone', models.CharField(blank=True, max_length=11, null=True, verbose_name='연락처')),
                ('school', models.CharField(blank=True, max_length=10, null=True, verbose_name='학교')),
                ('grade', models.CharField(blank=True, max_length=10, null=True, verbose_name='학년')),
                ('sClass', models.CharField(blank=True, max_length=10, null=True, verbose_name='반')),
                ('year', models.DateField(auto_now_add=True, null=True, verbose_name='연도')),
                ('is_activate', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name='pk')),
                ('question', models.CharField(blank=True, max_length=100, null=True, verbose_name='질문')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name='pk')),
                ('video', models.URLField(blank=True, null=True, verbose_name='영상 url')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolInfo',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name='pk')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name='pk')),
                ('userID', models.CharField(max_length=10, unique=True, verbose_name='아이디')),
                ('username', models.CharField(blank=True, max_length=10, null=True, verbose_name='유저이름')),
                ('password', models.CharField(max_length=20, verbose_name='비밀번호')),
                ('phone', models.CharField(blank=True, max_length=11, null=True, verbose_name='연락처')),
                ('school', models.CharField(blank=True, max_length=15, null=True, verbose_name='학교')),
                ('grade', models.IntegerField(blank=True, null=True, verbose_name='학년')),
                ('sClass', models.IntegerField(blank=True, null=True, verbose_name='반')),
                ('is_activate', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentQuestion',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name='pk')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_question', to='website.Question')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_question', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name='pk')),
                ('comment', models.CharField(blank=True, max_length=200, null=True, verbose_name='댓글')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='website.Report')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to=settings.AUTH_USER_MODEL)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='website.Teacher')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teacher', to='website.Teacher'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
