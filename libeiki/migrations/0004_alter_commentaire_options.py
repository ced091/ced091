# Generated by Django 5.1.2 on 2024-11-02 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libeiki', '0003_commentaire_date_com_commentaire_visible'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commentaire',
            options={'ordering': ['-date_com']},
        ),
    ]