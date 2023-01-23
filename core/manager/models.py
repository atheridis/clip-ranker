"""
Copyright (C) 2023  Georgios Atheridis <georgios@atheridis.org>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


class ResetData(models.Model):
    date_time = models.DateTimeField()
    end_date_time = models.DateTimeField(default=datetime.utcfromtimestamp(2147483640))
    max_clips = models.IntegerField(default=2)
    ranks = models.IntegerField(default=5)
    user_created_clip = models.BooleanField(default=True)
    clip_newer_than = models.DateTimeField(default=datetime.utcfromtimestamp(1))


class AllowedChannel(models.Model):
    broadcaster_id = models.CharField(max_length=100)
    reset_data = models.ForeignKey(ResetData, on_delete=models.CASCADE)

    class Meta:
        unique_together = (
            "broadcaster_id",
            "reset_data",
        )


class Clip(models.Model):
    id = models.CharField(primary_key=True, max_length=100, unique=True)
    url = models.URLField(null=True)
    embed_url = models.URLField(null=True)
    broadcaster_id = models.CharField(null=True, max_length=100)
    broadcaster_name = models.CharField(null=True, max_length=100)
    creator_id = models.CharField(null=True, max_length=100)
    creator_name = models.CharField(null=True, max_length=100)
    video_id = models.CharField(null=True, max_length=100)
    game_id = models.CharField(null=True, max_length=100)
    title = models.CharField(null=True, max_length=200)
    view_count = models.IntegerField(null=True)
    created_at = models.DateTimeField(null=True)
    thumbnail_url = models.URLField(null=True)
    duration = models.FloatField(null=True)
    vod_offset = models.IntegerField(null=True)
    date_added = models.DateTimeField(null=True)
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    rank = models.IntegerField(null=True)
