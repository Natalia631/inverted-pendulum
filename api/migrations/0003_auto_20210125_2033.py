# Generated by Django 3.1.5 on 2021-01-25 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210125_2006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='noisemodel',
            old_name='json',
            new_name='array',
        ),
    ]