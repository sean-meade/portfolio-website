# Generated by Django 5.0.2 on 2024-02-26 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_remove_project_tag_projecttag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projecttag',
            old_name='project_id',
            new_name='project',
        ),
        migrations.RenameField(
            model_name='projecttag',
            old_name='tag_id',
            new_name='tag',
        ),
    ]
