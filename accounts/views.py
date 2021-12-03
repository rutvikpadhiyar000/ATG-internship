from django.http.response import HttpResponse
from django.shortcuts import render
from allauth.socialaccount.models import SocialAccount, SocialToken
from .forms import ProfileForm
from .models import Profile
# Create your views here.


def show_profile(request):

    if request.method == 'POST':

        request.user.firstname = request.POST['first_name']
        request.user.last_name = request.POST['last_name']
        request.user.save()

        profilepic = request.POST['profilepic']
        address = request.POST['address']
        try:
            is_doctor = request.POST['is_doctor'] == 'on'
        except:
            is_doctor = False
        Profile.objects.create(
            user=request.user,
            profilepic=profilepic,
            address=address,
            is_doctor=is_doctor,
        )

    if Profile.objects.filter(user=request.user):
        return render(request, 'accounts/show_profile.html')

    form = ProfileForm()
    return render(request, 'accounts/create_profile.html', {'form': form})
