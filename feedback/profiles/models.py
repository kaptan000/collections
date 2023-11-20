from django.db import models
from django.views import View

# Create your models here.
class UserProfile(models.Model):
    image = models.ImageField(upload_to="images")



