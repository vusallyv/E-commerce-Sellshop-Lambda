# Generated by Django 3.2.7 on 2022-05-05 16:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0007_blog_typing_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='online_users',
            field=models.ManyToManyField(related_name='online_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
