# Generated by Django 3.1.6 on 2021-02-05 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdashboardmodule',
            name='column',
            field=models.PositiveBigIntegerField(verbose_name='column'),
        ),
        migrations.AlterField(
            model_name='userdashboardmodule',
            name='user',
            field=models.UUIDField(verbose_name='user'),
        ),
    ]