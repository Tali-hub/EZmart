# Generated by Django 3.1.4 on 2020-12-08 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0002_auto_20201207_0110'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='facebook_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='store',
            name='instagram_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='store',
            name='logo_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='store',
            name='twitter_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
