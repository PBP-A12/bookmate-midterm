from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Subject(models.Model) : 
    # model subject / genre sebuah buku 
    name = models.CharField(max_length=255)     # nama subject tersebut, misalnya 'science fiction'

    def __str__(self): 
        return f"<{self.id}> {self.name}"

class Member(models.Model) : 
    # model pengguna BookMate, dinamai Member supaya tidak ambigu dengan model User bawaan Django 
    account = models.OneToOneField(User, on_delete=models.CASCADE)                                      # username, email, dll menggunakan model User bawaan Django
    interest_subjects = models.ManyToManyField(Subject, related_name="interested_members", blank=True, default=None)  # subject-subject yang member sukai

    match_sent = models.ManyToManyField("self", blank=True, default=None)   #  match yang dikirim oleh member ini ke orang lain 
    match_received = models.ManyToManyField("self",  blank=True, default=None)   # match yang diterima oleh member ini dari orang lain
    

    def __str__(self): 
        return self.account.username