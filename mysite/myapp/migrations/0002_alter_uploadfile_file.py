# Generated by Django 3.2.8 on 2021-10-21 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='File',
            field=models.FileField(upload_to='media/'),
        ),
    ]
