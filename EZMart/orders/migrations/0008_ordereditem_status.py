# Generated by Django 3.1.3 on 2021-01-02 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20210102_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordereditem',
            name='status',
            field=models.CharField(default='Awaiting confirmation', max_length=100),
        ),
    ]
