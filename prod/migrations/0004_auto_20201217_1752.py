# Generated by Django 3.1.3 on 2020-12-17 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prod', '0003_auto_20201217_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sex',
            name='name',
            field=models.CharField(default='None', max_length=30, verbose_name='Пол'),
        ),
    ]