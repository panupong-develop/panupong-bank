# Generated by Django 4.1.1 on 2022-09-08 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_remove_incomingrequest_geoip"),
    ]

    operations = [
        migrations.RenameField(
            model_name="incomingrequest",
            old_name="created",
            new_name="dated",
        ),
        migrations.RemoveField(
            model_name="incomingrequest",
            name="updated",
        ),
    ]
