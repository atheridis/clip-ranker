from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Clip(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
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
    account = models.ForeignKey(User, on_delete=models.CASCADE)
