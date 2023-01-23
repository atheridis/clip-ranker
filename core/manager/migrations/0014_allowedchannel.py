# Generated by Django 4.1.5 on 2023-01-23 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("manager", "0013_resetdata_clip_limit_to_channels_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="AllowedChannel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("broadcaster_id", models.CharField(max_length=100)),
                (
                    "reset_data",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="manager.resetdata",
                    ),
                ),
            ],
        ),
    ]