# Generated by Django 4.1.5 on 2023-01-23 11:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("manager", "0012_resetdata_ranks"),
    ]

    operations = [
        migrations.AddField(
            model_name="resetdata",
            name="clip_limit_to_channels",
            field=models.JSONField(null=True),
        ),
        migrations.AddField(
            model_name="resetdata",
            name="clip_newer_than",
            field=models.DateTimeField(default=datetime.datetime(1970, 1, 1, 0, 0, 1)),
        ),
        migrations.AddField(
            model_name="resetdata",
            name="user_created_clip",
            field=models.BooleanField(default=True),
        ),
    ]
