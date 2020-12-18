from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    email = models.EmailField(max_length=255)
    profile_pic = models.ImageField(upload_to='customers', null=True, blank=True, default='avatar.jpg')

    def __str__(self):
        return self.name

    @property
    def profile_pic_url(self):
        if self.profile_pic and hasattr(self.profile_pic, 'url'):
            return self.profile_pic.url
    