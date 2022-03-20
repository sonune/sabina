from pyexpat import model
from django.db import models
from static import mainengine
from datetime import date

now = date.today()

class Uska_answer(models.Model):
    name = models.CharField(default=f'Sabina ka answer {now}',max_length=6000)
    days_left = models.CharField(default=mainengine.Condition() , max_length=10)
    # Mera_Question = models.CharField(max_length=600)
    Sabina_ka_Jawab_of_specifice_question = models.TextField()

    def __str__(self):
        return self.name
    def register(self):
        self.save()
    
    

    

class Mera_sawwal(models.Model):
    name = models.CharField(default= f'lucky ka Sawwal {now}', max_length=6000)
    Mera_Specific_sawwal = models.CharField(max_length=6000)

    def __str__(self):
        return self.name 
    def register(self):
        self.save()
    @staticmethod
    def get_My_latest_questions():
        return Mera_sawwal.objects.latest('id')
