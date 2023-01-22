import requests
from .models import Clip
from urllib.parse import urlparse
from allauth.socialaccount.models import SocialApp, SocialToken


def request_clip(url: str):
    id = urlparse(url).path.split("/")[-1]

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
    Clip(
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
    ).save()

    return
