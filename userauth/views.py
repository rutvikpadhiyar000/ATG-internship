from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth import authenticate, login, logout

from .models import Profile
from .forms import RegisterForm
# Create your views here.


def Login(request):
    if request.method == 'POST':
        context = {}
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            context['profile'] = user.profile
            return redirect("profile")
    elif request.user.is_authenticated:
        return redirect("profile")
    return render(request, 'userauth/login.html')


def Logout(request):
    logout(request)
    return redirect('login')


def userprofile(request):
    if request.user.is_authenticated:
        return render(request, 'userauth/profile.html')
    return redirect('login')


def Signup(request):

    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        print(user_form.errors)
        if user_form.is_valid():
            user = user_form.save()

            profilepic = request.FILES['profilepic']
            is_doctor = True if 'is_doctor' in request.POST else False
            address = request.POST['address']

            Profile.objects.create(
                user=user,
                profilepic=profilepic,
                is_doctor=is_doctor,
                address=address
            )
            return redirect('login')
        return HttpResponse('Invalid Data')
    elif request.user.is_authenticated:
        return redirect("profile")

    return render(request, 'userauth/signup.html')
