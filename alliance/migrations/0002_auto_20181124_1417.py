# Generated by Django 2.1.2 on 2018-11-24 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alliance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alliance',
            name='allianceLogo',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]