# Generated by Django 3.0.5 on 2020-07-06 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200629_1028'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'permissions': (('ver_dashboard', 'Pode acessar tela Dashboard'),)},
        ),
    ]