# Generated by Django 2.2 on 2021-03-23 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log_reg', '0003_auto_20210323_0953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='creator',
        ),
        migrations.DeleteModel(
            name='Assignment',
        ),
        migrations.DeleteModel(
            name='Class',
        ),
    ]
