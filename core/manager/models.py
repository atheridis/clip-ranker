from django.db import models


# Create your models here.
class Clip(models.Model):
    id = models.TextField(primary_key=True)
    url = models.URLField(null=True)
    embed_url = models.URLField(null=True)
    broadcaster_id = models.TextField(null=True)
    broadcaster_name = models.TextField(null=True)
    creator_id = models.TextField(null=True)
    creator_name = models.TextField(null=True)
    video_id = models.TextField(null=True)
    game_id = models.TextField(null=True)
    title = models.TextField(null=True)
    view_count = models.IntegerField(null=True)
    created_at = models.DateTimeField(null=True)
    thumbnail_url = models.TextField(null=True)
    duration = models.FloatField(null=True)
    vod_offset = models.IntegerField(null=True)
