# Generated by Django 5.1.6 on 2025-02-17 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='auccarsusa',
            name='commission',
            field=models.IntegerField(blank=True, null=True, verbose_name='Комиссия'),
        ),
        migrations.AlterField(
            model_name='auccarsusa',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Цена в РФ'),
        ),
    ]
