# Generated by Django 5.0.6 on 2024-06-23 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AreTheServersOk', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='server',
            old_name='ssh_adress',
            new_name='ip',
        ),
        migrations.AddField(
            model_name='server',
            name='username',
            field=models.CharField(default='root', max_length=200),
        ),
    ]
