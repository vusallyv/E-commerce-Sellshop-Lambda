# Generated by Django 3.2.7 on 2021-09-21 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Max 30 char.', max_length=30, verbose_name='Name')),
                ('email', models.EmailField(default='', max_length=254, verbose_name='Email Address')),
                ('message', models.TextField(verbose_name='Message')),
            ],
        ),
    ]
