# Generated by Django 4.1.5 on 2023-01-22 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("manager", "0008_resettime_clip_amount"),
    ]

    operations = [
        migrations.RenameField(
            model_name="resettime",
            old_name="clip_amount",
            new_name="max_clips",
        ),
    ]