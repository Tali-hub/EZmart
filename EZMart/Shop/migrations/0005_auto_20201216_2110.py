# Generated by Django 3.1.3 on 2020-12-16 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0004_store_logo_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='logo_img',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/'),
        ),
    ]
