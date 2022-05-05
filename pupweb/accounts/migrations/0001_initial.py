# Generated by Django 4.0.4 on 2022-05-05 11:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_id', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='User ID')),
                ('email', models.EmailField(max_length=120, unique=True, verbose_name='Email Address')),
                ('is_active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('is_regular', models.BooleanField(default=True)),
                ('first_name', models.CharField(max_length=80)),
                ('middle_name', models.CharField(blank=True, max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('birthday', models.DateField()),
                ('age', models.IntegerField()),
                ('branch', models.CharField(choices=[('MN', 'Manila'), ('TC', 'Taguig City'), ('QC', 'Quezon City'), ('SJ', 'San Juan City'), ('PC', 'Paranaque City')], max_length=2)),
                ('mobile_num', models.CharField(max_length=11)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dep_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('sub_code', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Subject Code')),
                ('year_level', models.IntegerField()),
                ('description', models.CharField(max_length=120)),
                ('units', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_sched', models.CharField(max_length=5)),
                ('time_sched', models.CharField(max_length=30)),
                ('admin_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='schedule_faculty', to=settings.AUTH_USER_MODEL, verbose_name='Faculty')),
                ('stud_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule_student', to=settings.AUTH_USER_MODEL, verbose_name='Student ID')),
            ],
        ),
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('final_grade', models.DecimalField(decimal_places=2, max_digits=3)),
                ('admin_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='grades_faculty', to=settings.AUTH_USER_MODEL, verbose_name='Faculty')),
                ('stud_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grades_student', to=settings.AUTH_USER_MODEL, verbose_name='Student ID')),
                ('sub_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.subject', verbose_name='Subject Code')),
            ],
        ),
    ]
