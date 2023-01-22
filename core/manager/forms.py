from django import forms


class ClipForm(forms.Form):
    clip = forms.CharField(label="clip", max_length=200)
