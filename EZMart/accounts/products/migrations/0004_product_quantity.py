# Generated by Django 3.1.3 on 2020-12-07 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_regulation'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]