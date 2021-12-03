from django.urls import path

from . import views
urlpatterns = [
    path('accounts/profile/', views.show_profile, name='show_profile')
]
