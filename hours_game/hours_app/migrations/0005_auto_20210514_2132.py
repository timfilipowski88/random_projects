# Generated by Django 2.2 on 2021-05-15 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hours_app', '0004_worklog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worklog',
            name='hours',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=100, null=True),
        ),
    ]
