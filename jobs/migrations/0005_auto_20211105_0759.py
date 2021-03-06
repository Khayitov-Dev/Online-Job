# Generated by Django 3.2.9 on 2021-11-05 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_recruiter_company'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recruiter',
            options={'verbose_name_plural': 'Recruiter'},
        ),
        migrations.AlterModelOptions(
            name='studentuser',
            options={'verbose_name_plural': 'StudentUser'},
        ),
        migrations.RemoveField(
            model_name='recruiter',
            name='company',
        ),
        migrations.AlterField(
            model_name='recruiter',
            name='image',
            field=models.ImageField(upload_to='student/'),
        ),
    ]
