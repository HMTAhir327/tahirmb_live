# Generated by Django 3.1.4 on 2021-02-14 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0009_marage_is_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relationship',
            name='receiver',
        ),
        migrations.RemoveField(
            model_name='relationship',
            name='sender',
        ),
        migrations.DeleteModel(
            name='Marage',
        ),
        migrations.DeleteModel(
            name='Relationship',
        ),
    ]
