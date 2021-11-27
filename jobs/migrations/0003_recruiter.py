# Generated by Django 3.2.9 on 2021-11-05 07:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0002_alter_studentuser_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recruiter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=15, null=True)),
                ('image', models.ImageField(upload_to='recruiter/')),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('unknown', 'unknown')], max_length=30, null=True)),
                ('type', models.CharField(max_length=255, null=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]