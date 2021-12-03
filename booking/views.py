from django.shortcuts import render
from datetime import timedelta
from dateutil import parser
from django.contrib.auth.models import User

from accounts.models import Profile
from .utils import connect_to_calendar, convert_RFC, prepare_event
from .models import Event
# Create your views here.


def show_doctors(request):
    all_doctors = Profile.objects.filter(is_doctor=True)
    return render(request, 'booking/show_doctors.html', {'doctors': all_doctors})


def book_appointment(request, doctor_mail):
    if request.method == 'POST':

        data = {}
        data['start_time'] = parser.parse(request.POST['start_time'])
        data['end_time'] = parser.parse(
            request.POST['start_time']) + timedelta(minutes=45)
        data['attendees'] = f'{request.user.email}, {doctor_mail}'
        data['speciality'] = request.POST['speciality']
        event = prepare_event(data)

        # For Patient Calender
        service = connect_to_calendar(user=request.user)
        res = service.events().insert(calendarId='primary', body=event).execute()

        # For Doctor Calender
        # doctor = User.objects.get(email=doctor_mail)
        # service = connect_to_calendar(user=request.user)
        # res = service.events().insert(calendarId='primary', body=event).execute()

    return render(request, 'booking/book_doctor.html', {'doctor_mail': doctor_mail})
