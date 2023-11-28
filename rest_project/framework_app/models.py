from django.db import models

# Create your models here.


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department = models.CharField(max_length=40)
    total_experience = models.IntegerField()

class Singer(models.Model):
    full_name = models.CharField(max_length=50)
    gender = models.CharField(choices=(('Male',"Male"),("Female","Female")),max_length=30)

    def __str__(self):
        return self.full_name

class Song(models.Model):
    title = models.CharField(max_length=50)  
    duration = models.IntegerField()
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE,related_name='song')      

    def __str__(self) -> str:
        return self.title