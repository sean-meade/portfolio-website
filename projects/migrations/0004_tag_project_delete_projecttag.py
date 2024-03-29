# Generated by Django 5.0.2 on 2024-02-26 21:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_tag_options_tag_friendly_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='projects.project'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ProjectTag',
        ),
    ]
