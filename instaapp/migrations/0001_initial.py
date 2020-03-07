# Generated by Django 2.1 on 2020-03-07 18:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('bio', models.CharField(max_length=200)),
                ('profile_pic', models.ImageField(default='DEFAULT VALUE', upload_to='photos/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('followers', models.ManyToManyField(blank=True, default=0, related_name='profile_followers', to='instaapp.Profile')),
                ('following', models.ManyToManyField(blank=True, default=0, related_name='profile_following', to='instaapp.Profile')),
            ],
        ),
    ]