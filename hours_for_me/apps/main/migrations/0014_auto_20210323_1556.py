# Generated by Django 2.2 on 2021-03-23 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20210323_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='due_date',
        ),
        migrations.RemoveField(
            model_name='collection',
            name='due_date',
        ),
    ]