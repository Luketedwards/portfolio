# Generated by Django 4.1.2 on 2022-11-11 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_project_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]
