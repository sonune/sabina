from datetime import date
from django.db import models
from static import mainengine
from datetime import date


now = date.today()



class Uska_Question(models.Model):
    # sort = models.IntegerField(default= mainengine.Condition(), max_length=10)
    name = models.CharField(default= f'Sabina ka Question {now}',max_length=6000)
    Uska_specific_question = models.CharField(max_length=6000)

    def __str__(self):
        return self.name 
    def register(self):
        self.save()
    @staticmethod
    def get_Uska_latest_question():
        return Uska_Question.objects.latest('id')
    
    
    

class Mera_Jawwab(models.Model):
    name = models.CharField(default= f'Mera Answers {now}',max_length=6000)
    MyAnswers = models.CharField(max_length=6000)

    def __str__(self):
        return self.name 
    def register(self):
        self.save()
    @staticmethod
    def get_Mera_latest_jawwab():
        return Mera_Jawwab.objects.latest('id')
    



    