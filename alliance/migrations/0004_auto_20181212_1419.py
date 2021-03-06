# Generated by Django 2.1.2 on 2018-12-12 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alliance', '0003_auto_20181211_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='sub_forums',
            field=models.ManyToManyField(blank=True, to='alliance.SubForum'),
        ),
        migrations.AlterField(
            model_name='subforum',
            name='topics',
            field=models.ManyToManyField(blank=True, to='alliance.Topic'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='posts',
            field=models.ManyToManyField(blank=True, to='alliance.PostForum'),
        ),
    ]
