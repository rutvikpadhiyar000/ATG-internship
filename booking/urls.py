from django.urls import path

from . import views
urlpatterns = [
    path('booking/doctors/', views.show_doctors, name='show_doctors'),
    path('booking/doctors/<str:doctor_mail>',
         views.book_appointment, name='book_appointment'),
]
