# Generated by Django 3.2.7 on 2021-09-24 09:12

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
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Max 30 char.', max_length=30, verbose_name='First Name')),
                ('last_name', models.CharField(help_text='Max 30 char.', max_length=30, verbose_name='Last Name')),
                ('email', models.EmailField(default='', max_length=254, verbose_name='Email Address')),
                ('country', models.CharField(default='', max_length=255, verbose_name='Country')),
                ('city', models.CharField(default='', max_length=30, verbose_name='City')),
                ('phone_number', models.CharField(default=0, max_length=255, verbose_name='Phone number')),
                ('additional_info', models.TextField(blank=True, default='', null=True, verbose_name='Additional Info')),
                ('password', models.CharField(default='', max_length=30, verbose_name='Password')),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Salary')),
            ],
        ),
    ]
