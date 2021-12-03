from django import forms

from .models import Profile
# creating a form


class ProfileForm(forms.Form):

    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    profilepic = forms.ImageField()
    address = forms.CharField(max_length=200)
    is_doctor = forms.BooleanField(required=False)
