# Generated by Django 5.0.2 on 2024-02-25 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='collaboration',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='under_construction',
            field=models.BooleanField(default=False),
        ),
    ]
