# Generated by Django 4.1.3 on 2024-03-21 23:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('telegram', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': 'Телеграм аккаунт', 'verbose_name_plural': 'Телеграм аккаунти'},
        ),
    ]
