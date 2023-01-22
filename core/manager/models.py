from django.db import models


# Create your models here.
class Clip(models.Model):
    id = models.TextField(primary_key=True)
    url = models.URLField()
    embed_url = models.URLField()
    broadcaster_id = models.TextField()
    broadcaster_name = models.TextField()
    creator_id = models.TextField()
    creator_name = models.TextField()
    video_id = models.TextField()
    game_id = models.TextField()
    title = models.TextField()
    view_count = models.IntegerField()
    created_at = models.TextField()
    thumbnail_url = models.TextField()
    duration = models.FloatField()
    vod_offset = models.IntegerField()
