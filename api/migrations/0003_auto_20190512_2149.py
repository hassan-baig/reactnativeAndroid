# Generated by Django 2.2 on 2019-05-12 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190512_1944'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaint',
            old_name='jobType',
            new_name='jobtype',
        ),
    ]