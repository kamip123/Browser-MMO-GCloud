# Generated by Django 2.1.2 on 2018-11-24 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0007_auto_20181119_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='prfilePic',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
