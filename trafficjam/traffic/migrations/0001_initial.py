# Generated by Django 2.1.2 on 2019-03-21 10:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name_plural': 'Cities',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(default='', max_length=900)),
                ('date_and_time', models.DateTimeField(default=datetime.datetime(2019, 3, 21, 16, 32, 26, 278004))),
            ],
            options={
                'verbose_name_plural': 'Comment',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=60)),
                ('email', models.EmailField(default='', max_length=100)),
                ('message', models.TextField(default='', max_length=900)),
            ],
            options={
                'verbose_name_plural': ' Contact ',
            },
        ),
        migrations.CreateModel(
            name='postcreate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=60)),
                ('place_name', models.CharField(default='', max_length=200)),
                ('trafficjam_details', models.TextField(default='', max_length=900)),
                ('date_and_time', models.DateTimeField(default=datetime.datetime(2019, 3, 21, 16, 32, 26, 250501))),
            ],
            options={
                'verbose_name_plural': ' Post_create ',
            },
        ),
    ]
