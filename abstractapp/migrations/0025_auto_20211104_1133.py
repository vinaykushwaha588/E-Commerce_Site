# Generated by Django 3.2.8 on 2021-11-04 16:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abstractapp', '0024_auto_20211104_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_time',
            field=models.TimeField(default=datetime.datetime(2021, 11, 4, 11, 33, 0, 980346)),
        ),
        migrations.AlterField(
            model_name='order',
            name='prize',
            field=models.IntegerField(max_length=5),
        ),
    ]
