from django.db import models
from django.contrib.auth.models import User


class ResetData(models.Model):
    date_time = models.DateTimeField()
    max_clips = models.IntegerField(default=2)
    ranks = models.IntegerField(default=5)


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
