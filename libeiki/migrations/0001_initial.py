# Generated by Django 4.0.4 on 2024-01-28 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pseudo', models.CharField(max_length=50)),
                ('note', models.FloatField()),
                ('texte', models.TextField()),
            ],
        ),
    ]
