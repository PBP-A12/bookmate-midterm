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

    match_sent = models.ManyToManyField("self", blank=True, symmetrical=False, related_name="sent_matches")     #  match yang dikirim oleh member ini ke orang lain 
    match_received = models.ManyToManyField("self", blank=True, symmetrical=False, related_name="received_matches") # match yang diterima oleh member ini dari orang lain
    
    # akses review dan request pake related_name dari models masing2 aja
    # https://stackoverflow.com/questions/2642613/what-is-related-name-used-for
    # reviews     
    # requests 

    def __str__(self): 
        return self.account.username