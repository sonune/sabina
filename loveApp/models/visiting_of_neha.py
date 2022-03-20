from django.db import models
from static import mainengine
from datetime import date

now = date.today()

daysleft = 'I love Sabina and days_left is' + str(now)
currenttime = now.strftime("%H:%M:%S not accurate")



class Attendence(models.Model):
    name = models.CharField(default = now, max_length=499)
    I_am_there_lucky = models.CharField(max_length=100)
    Time = models.CharField(max_length=50 , default=currenttime)
    
    def register(self):
        self.save()
    def __str__(self):
        return self.name
    