# Generated by Django 5.1 on 2024-09-28 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Espace_CT', '0012_minecraftserver_rcon_port'),
    ]

    operations = [
        migrations.AddField(
            model_name='minecraftserver',
            name='server_port',
            field=models.CharField(default='25565', max_length=5),
        ),
    ]