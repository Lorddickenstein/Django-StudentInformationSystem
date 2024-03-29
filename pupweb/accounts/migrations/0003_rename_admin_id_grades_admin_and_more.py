# Generated by Django 4.0.4 on 2022-08-29 14:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_course_rename_description_department_dep_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grades',
            old_name='admin_id',
            new_name='admin',
        ),
        migrations.RenameField(
            model_name='grades',
            old_name='stud_id',
            new_name='stud',
        ),
        migrations.RenameField(
            model_name='grades',
            old_name='sub_code',
            new_name='sub',
        ),
        migrations.RenameField(
            model_name='schedule',
            old_name='admin_id',
            new_name='admin',
        ),
        migrations.RenameField(
            model_name='schedule',
            old_name='stud_id',
            new_name='stud',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='course_id',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='dep_id',
            new_name='dep',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='stud_id',
            new_name='stud',
        ),
        migrations.AlterField(
            model_name='student',
            name='year_level',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(8)], verbose_name='Year Level'),
        ),
    ]
