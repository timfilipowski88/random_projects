# Generated by Django 2.2 on 2021-03-23 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210323_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='due_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='class',
            name='due_date',
            field=models.DateField(),
        ),
    ]
