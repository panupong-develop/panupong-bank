# Generated by Django 4.1.1 on 2022-09-08 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_alter_incomingrequest_geoip_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="incomingrequest",
            name="geoip",
        ),
    ]
