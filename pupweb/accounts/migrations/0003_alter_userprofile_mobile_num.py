# Generated by Django 4.0.4 on 2022-05-06 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_grades_admin_id_alter_grades_final_grade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='mobile_num',
            field=models.CharField(blank=True, max_length=11),
        ),
    ]
