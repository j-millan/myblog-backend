# Generated by Django 3.2.5 on 2021-08-08 00:08

import auth.models
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
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(blank=True, max_length=350, null=True, verbose_name='biography')),
                ('profile_picture', models.ImageField(default='img/profile-pictures/default.jpg', upload_to=auth.models.profile_picture_upload_location)),
                ('youtube', models.URLField(blank=True, max_length=150, null=True, verbose_name='youtube channel')),
                ('instagram', models.URLField(blank=True, max_length=150, null=True, verbose_name='instagram page')),
                ('twitter', models.URLField(blank=True, max_length=150, null=True, verbose_name='twitter page')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
