from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile


class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    first_name = forms.CharField(max_length=100,
                                 required=True)

    last_name = forms.CharField(max_length=100,
                                required=True)

    username = forms.CharField(max_length=100,
                               required=True)

    email = forms.EmailField(required=True)

    password1 = forms.CharField(max_length=50,
                                required=True)

    password2 = forms.CharField(max_length=50,
                                required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']


class CreateProfileForm(forms.ModelForm):
    profilepic = forms.ImageField()
    is_doctor = forms.BooleanField()

    class Meta:
        model = Profile
        fields = ['profilepic', 'is_doctor']
