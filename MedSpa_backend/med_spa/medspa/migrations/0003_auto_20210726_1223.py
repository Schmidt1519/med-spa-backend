# Generated by Django 3.1.8 on 2021-07-26 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medspa', '0002_auto_20210726_1158'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reviews',
            new_name='Review',
        ),
    ]