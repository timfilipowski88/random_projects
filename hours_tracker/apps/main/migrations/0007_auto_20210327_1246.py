# Generated by Django 2.2 on 2021-03-27 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210323_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='completed',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='collection',
            name='completed',
            field=models.BooleanField(),
        ),
    ]
