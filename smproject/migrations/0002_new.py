# Generated by Django 4.1.5 on 2023-02-14 18:55

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('smproject', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('news_category', models.CharField(max_length=20)),
                ('news_topic', models.CharField(max_length=100)),
                ('news_details', models.CharField(max_length=2000)),
                ('news_created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('news_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
