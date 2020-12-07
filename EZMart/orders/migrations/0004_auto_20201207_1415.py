# Generated by Django 3.1.3 on 2020-12-07 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_regulation'),
        ('orders', '0003_auto_20201207_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordereditem',
            name='product',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product'),
        ),
    ]