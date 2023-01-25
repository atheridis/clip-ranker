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
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.sites.models import Site

from .request_clip import request_clip
from .forms import ClipForm, RankForm
from .errors import (
    TooManyClipsError,
    TooLateError,
    ChannelNotAllowedError,
    UserNotCreatedClipError,
    ClipTooOldError,
    BadRequestError,
    UnauthorizedError,
    NotFoundError,
)
from .models import Clip, ResetData


@staff_member_required
def show_clips(request, id):
    reset_data = ResetData.objects.latest("date_time")
    reset_time = reset_data.date_time
    try:
        video = Clip.objects.filter(date_added__gt=reset_time).order_by("date_added")[
            id - 1
        ]
    except IndexError:
        return redirect(final_ranking)
    if request.method == "POST":
        form = RankForm(request.POST)
        if form.is_valid():
            video.rank = form.cleaned_data["value"]
            video.save()
            return redirect(show_clips, id=id + 1)
    return render(
        request,
        "manager/clip_viewer.html",
        context={
            "video": video,
            "ranks": range(reset_data.ranks, 0, -1),
            "sites": Site.objects.all(),
        },
    )


@staff_member_required
def final_ranking(request):
    reset_data = ResetData.objects.latest("date_time")
    reset_time = reset_data.date_time
    return render(
        request,
        "manager/final.html",
        context={
            "videos": Clip.objects.filter(date_added__gt=reset_time),
            "ranks": range(reset_data.ranks, 0, -1),
            "sites": Site.objects.all(),
        },
    )


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ClipForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            try:
                request_clip(user=request.user, clip=form.cleaned_data["clip"])
            except ValidationError:
                message = "Sorry, clip already exists. Please send another clip."
            except TooManyClipsError:
                message = "Sorry, you have already reached the clip limit."
            except TooLateError:
                message = "Sorry, the deadline for posting has passed"
            except ChannelNotAllowedError:
                message = "Sorry, you're not allowed to send a clip from that channel."
            except UserNotCreatedClipError:
                message = "Sorry, you need to be the one who has created the clip."
            except ClipTooOldError:
                message = "Sorry, the clip is too old. Please send a newer clip."
            except BadRequestError:
                message = "Sorry, a bad request happened on our side."
            except UnauthorizedError:
                message = "We couldn't connect to twitch servers. Try logging out and logging back in."
            except NotFoundError:
                message = "Sorry, we couldn't find that twitch clip. Make sure to check the url."
            except Exception:
                message = "Something went wrong."
            else:
                message = "Thank you for submitting a clip."
            return render(request, "manager/index.html", {"message": message})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ClipForm()

    return render(request, "manager/index.html", {"form": form})
