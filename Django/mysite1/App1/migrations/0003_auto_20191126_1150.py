# Generated by Django 2.2.7 on 2019-11-26 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0002_auto_20191126_1146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accessrecord',
            old_name='date',
            new_name='data',
        ),
    ]
