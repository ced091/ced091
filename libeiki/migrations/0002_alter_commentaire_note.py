# Generated by Django 4.0.4 on 2024-02-03 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libeiki', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentaire',
            name='note',
            field=models.IntegerField(),
        ),
    ]
