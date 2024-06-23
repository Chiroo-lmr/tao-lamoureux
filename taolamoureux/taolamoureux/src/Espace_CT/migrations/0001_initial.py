# Generated by Django 5.0.6 on 2024-06-01 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=350)),
                ('url_placeholder', models.CharField(default='lien', max_length=100)),
                ('url', models.URLField()),
                ('priority', models.IntegerField(default=0)),
            ],
        ),
    ]
