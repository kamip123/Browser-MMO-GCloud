# Generated by Django 2.1.2 on 2018-10-26 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0004_server'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='playerAmount',
            field=models.IntegerField(),
        ),
    ]
