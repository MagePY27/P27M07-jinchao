# Generated by Django 2.2 on 2020-05-24 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0002_auto_20200524_2257'),
    ]

    operations = [
        migrations.RenameField(
            model_name='type',
            old_name='instance_project_type',
            new_name='project_type',
        ),
    ]
