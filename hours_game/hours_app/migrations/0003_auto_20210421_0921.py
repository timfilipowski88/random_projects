# Generated by Django 2.2 on 2021-04-21 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hours_app', '0002_auto_20210331_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='days_available',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='due_date',
            field=models.DateField(max_length=100, null=True),
        ),
    ]
