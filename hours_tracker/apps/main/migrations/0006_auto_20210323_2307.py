# Generated by Django 2.2 on 2021-03-24 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210323_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='completed',
            field=models.BooleanField(default=False, verbose_name='completed'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='completed',
            field=models.BooleanField(default=False, verbose_name='completed'),
        ),
    ]
