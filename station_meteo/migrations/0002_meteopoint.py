# Generated by Django 4.0.4 on 2024-02-17 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('station_meteo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeteoPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField()),
                ('humidity', models.FloatField()),
                ('pressure', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
