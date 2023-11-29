# Generated by Django 4.1.5 on 2023-02-15 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smproject', '0002_new'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=1000)),
                ('commentator', models.CharField(max_length=100)),
                ('commentator_position', models.CharField(max_length=50)),
            ],
        ),
    ]