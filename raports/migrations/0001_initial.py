# Generated by Django 2.1.2 on 2018-11-19 21:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('alliance', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cityMap', '0005_hinfantry_htanks_infantry_ltanks_motorized_planes'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllianceInvite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='alliance invite', max_length=100)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('alliance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='alliance.Alliance')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiverair', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='senderair', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BattleRaport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='battla raport', max_length=100)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('stolen_food', models.IntegerField(default=0)),
                ('stolen_energy', models.IntegerField(default=0)),
                ('stolen_minerals', models.IntegerField(default=0)),
                ('stolen_special_resource', models.IntegerField(default=0)),
                ('infantryA', models.IntegerField(default=0)),
                ('hinfantryA', models.IntegerField(default=0)),
                ('planesA', models.IntegerField(default=0)),
                ('ltanksA', models.IntegerField(default=0)),
                ('htanksA', models.IntegerField(default=0)),
                ('motorizedA', models.IntegerField(default=0)),
                ('infantryD', models.IntegerField(default=0)),
                ('hinfantryD', models.IntegerField(default=0)),
                ('planesD', models.IntegerField(default=0)),
                ('ltanksD', models.IntegerField(default=0)),
                ('htanksD', models.IntegerField(default=0)),
                ('motorizedD', models.IntegerField(default=0)),
                ('infantryAS', models.IntegerField(default=0)),
                ('hinfantryAS', models.IntegerField(default=0)),
                ('planesAS', models.IntegerField(default=0)),
                ('ltanksAS', models.IntegerField(default=0)),
                ('htanksAS', models.IntegerField(default=0)),
                ('motorizedAS', models.IntegerField(default=0)),
                ('infantryDS', models.IntegerField(default=0)),
                ('hinfantryDS', models.IntegerField(default=0)),
                ('planesDS', models.IntegerField(default=0)),
                ('ltanksDS', models.IntegerField(default=0)),
                ('htanksDS', models.IntegerField(default=0)),
                ('motorizedDS', models.IntegerField(default=0)),
                ('attacker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attacker', to=settings.AUTH_USER_MODEL)),
                ('cityA', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attackvillage', to='cityMap.CityOwned')),
                ('cityD', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='defensevillage', to='cityMap.CityOwned')),
                ('defender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='defender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HelpRaport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='help report', max_length=100)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cityhr', to='cityMap.CityOwned')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiverhr', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='senderhr', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SpecialResourceRaport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='resource report', max_length=100)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='citysrr', to='cityMap.CityOwned')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiversrr', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TradeRaport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='trade report', max_length=100)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='citytr', to='cityMap.CityOwned')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receivertr', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sendertr', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]