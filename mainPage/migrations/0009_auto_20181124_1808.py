# Generated by Django 2.1.2 on 2018-11-24 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0008_auto_20181124_1347'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='prfilePic',
            new_name='profilePic',
        ),
    ]
