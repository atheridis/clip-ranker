from django import forms


class RankForm(forms.Form):
    value = forms.IntegerField(label="rank")


class ClipForm(forms.Form):
    clip = forms.CharField(label="clip", max_length=200)
