# Generated by Django 5.1 on 2024-10-27 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Espace_CT', '0013_minecraftserver_server_port'),
    ]

    operations = [
        migrations.CreateModel(
            name='CloudTravail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('link', models.CharField(default='https://www.office.com/launch/powerpoint?wdOrigin=MARKETING.POWERPOINT.SIGNIN&auth=1', max_length=500)),
            ],
        ),
    ]
