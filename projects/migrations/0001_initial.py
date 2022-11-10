# Generated by Django 4.1.2 on 2022-11-10 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='typeOfApp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('url', models.URLField(blank=True)),
                ('date', models.DateTimeField(blank=True, default='2012-06-30T20:00:00.000000000-0400')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='')),
                ('category', models.CharField(blank=True, max_length=100)),
                ('skills', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.typeofapp')),
            ],
        ),
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.TextField()),
                ('date', models.DateTimeField(blank=True, default='2012-06-30T20:00:00.000000000-0400')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
        ),
    ]
