import requests

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .request_clip import request_clip
from .forms import ClipForm


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ClipForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            try:
                request_clip(form.cleaned_data.get("clip"))
            except Exception as e:
                print(e)
                return HttpResponse(b"<h1>NOPE</h1>")
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponse(b"<h1>THANKS</h1>")
            # return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ClipForm()

    return render(request, "name.html", {"form": form})
