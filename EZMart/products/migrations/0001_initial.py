# Generated by Django 3.1.3 on 2020-12-06 22:39

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField(default=0)),
                ('category', models.CharField(choices=[('E', 'Electronics'), ('FS', 'Food Stuff'), ('T', 'Tools')], max_length=2)),
                ('description', models.CharField(max_length=200)),
                ('active', models.BooleanField(default=True)),
                ('time_stamp', models.DateTimeField(auto_now=True, verbose_name='Time Stamp')),
                ('store', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Shop.store')),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]