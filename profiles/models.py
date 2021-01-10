from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    username = models.CharField(max_length=250, blank=True, null=True)
    first_name = models.CharField(max_length=250, blank=True, null=True)
    last_name = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField()
    about = models.TextField(blank=True, null=True)
    address = models.CharField(blank=True, null=True, max_length=250)
    phone_number = PhoneNumberField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Service(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    text = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name
    
class Skill(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    level = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user} --> {self.name} {self.level}%'
