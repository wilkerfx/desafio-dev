# Generated by Django 3.2.8 on 2021-10-26 07:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_auto_20211026_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadform',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 26, 7, 22, 28, 26308, tzinfo=utc)),
        ),
    ]
