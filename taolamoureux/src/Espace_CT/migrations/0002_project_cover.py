# Generated by Django 5.0.6 on 2024-06-01 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Espace_CT', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='cover',
            field=models.ImageField(default='missing-file.jpg', upload_to='mediadb/'),
        ),
    ]
