import requests
import datetime
from .errors import TooManyClips
from .models import Clip, ResetData
from urllib.parse import urlparse
from allauth.socialaccount.models import SocialApp, SocialToken
from django.contrib.auth.models import User


def request_clip(user, clip: str):
    id = urlparse(clip).path.split("/")[-1]
    user = User.objects.get(id=user.id)
    reset_data = ResetData.objects.first()
    reset_time = reset_data.date_time
    max_clips = reset_data.max_clips

    if (
        len(
            Clip.objects.filter(account=user).filter(
                date_added__gt=reset_time
            )
        )
        >= max_clips
    ):
        raise TooManyClips

    social_app: SocialApp = SocialApp.objects.first()
    oauth = SocialToken.objects.first().token
    client_id = social_app.client_id

    r = requests.get(
        "https://api.twitch.tv/helix/clips",
        headers={
            "Authorization": f"Bearer {oauth}",
            "Client-Id": f"{client_id}",
        },
        params={"id": id},
    )

    if r.status_code != 200:
        raise Exception

    data = r.json()["data"][0]
    print(data)
    clip = Clip(
        id=data["id"],
        url=data["url"],
        embed_url=data["embed_url"],
        broadcaster_id=data["broadcaster_id"],
        broadcaster_name=data["broadcaster_name"],
        creator_id=data["creator_id"],
        creator_name=data["creator_name"],
        video_id=data["video_id"],
        game_id=data["game_id"],
        title=data["title"],
        view_count=data["view_count"],
        created_at=data["created_at"],
        thumbnail_url=data["thumbnail_url"],
        duration=data["duration"],
        vod_offset=data["vod_offset"],
        date_added=datetime.datetime.now(),
        account=user,
    )
    clip.validate_unique()
    clip.save()

    return
