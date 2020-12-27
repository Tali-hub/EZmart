# Generated by Django 3.1.3 on 2020-12-27 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20201220_1553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordereditem',
            name='buyer',
        ),
        migrations.RemoveField(
            model_name='ordereditem',
            name='product',
        ),
        migrations.RemoveField(
            model_name='ordereditem',
            name='seller',
        ),
        migrations.AddField(
            model_name='ordereditem',
            name='buyer_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ordereditem',
            name='product_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ordereditem',
            name='seller_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
