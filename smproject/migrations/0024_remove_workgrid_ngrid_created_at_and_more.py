# Generated by Django 4.1.5 on 2023-02-26 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smproject', '0023_workgrid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workgrid',
            name='ngrid_created_at',
        ),
        migrations.RemoveField(
            model_name='workgrid',
            name='ngrid_user',
        ),
    ]