# Generated by Django 3.2.8 on 2021-10-18 20:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abstractapp', '0013_auto_20211018_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_time',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 15, 26, 54, 438528)),
        ),
        migrations.AlterField(
            model_name='user',
            name='cuntry',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]