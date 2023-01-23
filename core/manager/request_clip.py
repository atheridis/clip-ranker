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
import requests
import datetime
import pytz
from .errors import TooManyClipsError, TooLateError, ChannelNotAllowedError, UserNotCreatedClipError, ClipTooOldError
from .models import Clip, ResetData
from urllib.parse import urlparse
from allauth.socialaccount.models import SocialApp, SocialToken, SocialAccount
from django.contrib.auth.models import User


def request_clip(user, clip: str):
    id = urlparse(clip).path.split("/")[-1]
    user = User.objects.get(id=user.id)
    reset_data = ResetData.objects.latest('date_time')
    reset_time = reset_data.date_time
    max_clips = reset_data.max_clips

    if reset_data.end_date_time < datetime.datetime.now(pytz.utc):
        raise TooLateError

    if (
        len(
            Clip.objects.filter(account=user).filter(
                date_added__gt=reset_time
            )
        )
        >= max_clips
    ):
        raise TooManyClipsError

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

    if reset_data.user_created_clip:
        if not SocialAccount.objects.get(user=user).uid == data["creator_id"]:
            raise UserNotCreatedClipError

    if reset_data.allowedchannel_set.count() != 0:
        allowed_channels = reset_data.allowedchannel_set.filter(broadcaster_id=data["broadcaster_id"])
        if not allowed_channels.exists():
            raise ChannelNotAllowedError

    if (
            reset_data.clip_newer_than
            > datetime.datetime.strptime(data["created_at"], "%Y-%m-%dT%H:%M:%S%z")
    ):
        raise ClipTooOldError

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
        date_added=datetime.datetime.now(pytz.utc),
        account=user,
    )
    clip.validate_unique()
    clip.save()

    return
