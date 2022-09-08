# Generated by Django 4.1.1 on 2022-09-08 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_alter_incomingrequest_geoip_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="incomingrequest",
            name="geoip",
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name="incomingrequest",
            name="ipinfo",
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name="incomingrequest",
            name="ipware",
            field=models.JSONField(default=dict),
        ),
    ]