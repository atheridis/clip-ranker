import requests

from django.http import HttpResponse
from django.shortcuts import render
from django.core.exceptions import ValidationError

from .request_clip import request_clip
from .forms import ClipForm
from .errors import TooManyClips


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
