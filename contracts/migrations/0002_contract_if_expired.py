# Generated by Django 2.2.6 on 2019-11-19 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='if_expired',
            field=models.BooleanField(default=False),
        ),
    ]