# Generated by Django 2.2.7 on 2019-11-26 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accessrecord',
            old_name='data',
            new_name='date',
        ),
    ]
