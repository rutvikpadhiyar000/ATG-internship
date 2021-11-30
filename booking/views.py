from django.shortcuts import render, HttpResponse

# Create your views here.


def show_doctors(request):
    return render(request, 'booking/show_doctors.html')


def book_appointment(request):
    return HttpResponse("Book-Appointment Form Here")
