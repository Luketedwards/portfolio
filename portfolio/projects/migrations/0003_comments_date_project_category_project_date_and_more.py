# Generated by Django 4.1.2 on 2022-11-01 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='date',
            field=models.DateTimeField(blank=True, default='2012-06-30T20:00:00.000000000-0400'),
        ),
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='date',
            field=models.DateTimeField(blank=True, default='2012-06-30T20:00:00.000000000-0400'),
        ),
        migrations.AddField(
            model_name='project',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='project',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='project',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
