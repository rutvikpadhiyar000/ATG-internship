from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profilepic = models.ImageField(upload_to='user_images')
    is_doctor = models.BooleanField(default=False)
    address = models.CharField(max_length=500, null=True)

    def __str__(self) -> str:
        return self.user.username
