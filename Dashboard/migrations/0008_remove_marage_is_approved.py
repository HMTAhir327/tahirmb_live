# Generated by Django 3.1.4 on 2021-02-14 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0007_marage_is_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marage',
            name='is_approved',
        ),
    ]
