# Generated by Django 3.1.3 on 2020-12-16 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Basic', '0003_auto_20201216_2128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='form',
            name='user',
        ),
    ]
