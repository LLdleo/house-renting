# Generated by Django 2.2.6 on 2019-12-07 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='faculty',
            new_name='dept',
        ),
    ]