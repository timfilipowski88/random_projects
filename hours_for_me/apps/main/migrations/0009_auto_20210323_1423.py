# Generated by Django 2.2 on 2021-03-23 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('log_reg', '0004_auto_20210323_1143'),
        ('main', '0008_auto_20210323_1417'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('due_date', models.DateField()),
                ('completed', models.BooleanField(default=False)),
                ('priority', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_collections', to='log_reg.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='assignment',
            name='assignment_class',
        ),
        migrations.DeleteModel(
            name='Class',
        ),
        migrations.AddField(
            model_name='assignment',
            name='collection',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='owns_assignments', to='main.Collection'),
            preserve_default=False,
        ),
    ]
