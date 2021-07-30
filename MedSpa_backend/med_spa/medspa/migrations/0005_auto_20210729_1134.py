# Generated by Django 3.1.8 on 2021-07-29 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medspa', '0004_remove_cart_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='service_name',
        ),
        migrations.AddField(
            model_name='service',
            name='name',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='picture',
            field=models.CharField(default=None, max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.CharField(max_length=300),
        ),
    ]