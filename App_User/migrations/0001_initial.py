# Generated by Django 4.2.10 on 2024-02-15 06:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pics')),
                ('designation', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.TextField(blank=True, max_length=255, null=True)),
                ('bio', models.TextField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]