# Generated by Django 2.2 on 2020-05-24 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='host',
            name='instance_project_type',
        ),
        migrations.AddField(
            model_name='type',
            name='instance_project_type',
            field=models.CharField(choices=[('Develop', '开发中'), ('Maintain', '运维中')], default='Maintain', max_length=16, verbose_name='实例项目阶段'),
        ),
        migrations.AlterField(
            model_name='type',
            name='name',
            field=models.CharField(max_length=100, verbose_name='涉密名称'),
        ),
        migrations.AlterField(
            model_name='type',
            name='name_cn',
            field=models.CharField(max_length=100, verbose_name='交流名称'),
        ),
    ]