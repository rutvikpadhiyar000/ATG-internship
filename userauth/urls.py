from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
urlpatterns = [
    path('login', views.Login, name='login'),
    path('signup', views.Signup, name='signup'),
    path('logout', views.Logout, name='logout'),
    path('profile', views.userprofile, name='profile'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
