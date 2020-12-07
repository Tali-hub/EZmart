# Generated by Django 3.1.3 on 2020-12-06 23:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20201207_0110'),
        ('orders', '0002_auto_20201207_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordereditem',
            name='product',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Product', to='products.product'),
        ),
    ]