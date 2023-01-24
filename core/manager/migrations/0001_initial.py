# Generated by Django 4.1.5 on 2023-01-25 14:32

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ResetData",
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
                ("date_time", models.DateTimeField()),
                (
                    "end_date_time",
                    models.DateTimeField(default=datetime.datetime(2038, 1, 19, 3, 14)),
                ),
                ("max_clips", models.IntegerField(default=2)),
                ("ranks", models.IntegerField(default=5)),
                ("user_created_clip", models.BooleanField(default=True)),
                (
                    "clip_newer_than",
                    models.DateTimeField(
                        default=datetime.datetime(1970, 1, 1, 0, 0, 1)
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Clip",
            fields=[
                (
                    "id",
                    models.CharField(
                        max_length=100, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("url", models.URLField(null=True)),
                ("embed_url", models.URLField(null=True)),
                ("broadcaster_id", models.CharField(max_length=100, null=True)),
                ("broadcaster_name", models.CharField(max_length=100, null=True)),
                ("creator_id", models.CharField(max_length=100, null=True)),
                ("creator_name", models.CharField(max_length=100, null=True)),
                ("video_id", models.CharField(max_length=100, null=True)),
                ("game_id", models.CharField(max_length=100, null=True)),
                ("title", models.CharField(max_length=200, null=True)),
                ("view_count", models.IntegerField(null=True)),
                ("created_at", models.DateTimeField(null=True)),
                ("thumbnail_url", models.URLField(null=True)),
                ("duration", models.FloatField(null=True)),
                ("vod_offset", models.IntegerField(null=True)),
                ("date_added", models.DateTimeField(null=True)),
                ("rank", models.IntegerField(null=True)),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
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
            options={
                "unique_together": {("broadcaster_id", "reset_data")},
            },
        ),
    ]
