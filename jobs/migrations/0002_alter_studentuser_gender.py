# Generated by Django 3.2.9 on 2021-11-05 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentuser',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female'), ('unknown', 'unknown')], max_length=30, null=True),
        ),
    ]
