# Generated by Django 4.1.5 on 2023-01-22 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("manager", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="clip",
            old_name="user",
            new_name="account",
        ),
    ]
