# Generated by Django 3.1.3 on 2020-11-29 19:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(max_length=300, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_username', message='Username must be alphanumeric or contain numbers', regex='^[a-zA-Z0-9.+-]*$')])),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('data_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('first_name', models.CharField(default=None, max_length=30)),
                ('last_name', models.CharField(default=None, max_length=30)),
                ('address', models.CharField(default=None, max_length=150)),
                ('phone', models.CharField(default=None, max_length=14)),
                ('businessNum', models.CharField(default=None, max_length=14)),
                ('businessType', models.CharField(default=None, max_length=30)),
                ('store_ID', models.IntegerField(default=None, max_length=14)),
                ('is_business', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
