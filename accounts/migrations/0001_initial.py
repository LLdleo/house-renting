# Generated by Django 2.2.6 on 2019-11-14 18:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phoneNumber', models.TextField(blank=True, max_length=30)),
                ('faculty', models.TextField(blank=True, max_length=200)),
                ('academicYear', models.TextField(blank=True, null=True)),
                ('gender', models.TextField(blank=True, max_length=10)),
                ('dateOfBirth', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
