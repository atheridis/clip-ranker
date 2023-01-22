from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.contrib.admin.views.decorators import staff_member_required

from .request_clip import request_clip
from .forms import ClipForm, RankForm
from .errors import TooManyClips
from .models import Clip, ResetData


@staff_member_required
def show_clips(request, id):
    reset_data = ResetData.objects.first()
    reset_time = reset_data.date_time
    try:
        video = Clip.objects.filter(date_added__gt=reset_time)[id - 1]
    except IndexError:
        print("hi")
        return redirect(final_ranking)
    if request.method == "POST":
        form = RankForm(request.POST)
        if form.is_valid():
            print(f"post: {id} | {form.cleaned_data['value']}")
            video.rank = form.cleaned_data["value"]
            video.save()
            return redirect(show_clips, id=id + 1)
    return render(request, "manager/clip_viewer.html", context={
        "video": video,
    })


@staff_member_required
def final_ranking(request):
    reset_data = ResetData.objects.first()
    reset_time = reset_data.date_time
    return render(request, "manager/final.html", context={
        "videos": Clip.objects.filter(date_added__gt=reset_time),
    })


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ClipForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            try:
                request_clip(user=request.user, clip=form.cleaned_data["clip"])
            except ValidationError as e:
                print(e)
                return HttpResponse(b"<h1>Clip already exists</h1>")
            except TooManyClips:
                return HttpResponse(b"<h1>You have submitted the maximum number of clips</h1>")
            except Exception as e:
                print(e)
                return HttpResponse(b"<h1>NOPE</h1>")
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponse(b"<h1>THANKS</h1>")
            # return HttpResponseRedirect("/thanks/")
        else:
            print("invalid")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ClipForm()

    return render(request, "manager/index.html", {"form": form})
