# Generated by Django 3.1.8 on 2021-07-28 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medspa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='end_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='start_time',
            field=models.TimeField(null=True),
        ),
    ]
