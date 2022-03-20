from multiprocessing.sharedctypes import Value
from django.db import models
from static import mainengine


class UskaMassage(models.Model):
    sort = models.CharField(default= mainengine.Condition(), max_length=10)
    # date = models.DateField()
    repeated_questions_ka_answer = models.CharField(max_length=300)
    kaisi_ho_ka_answer = models.CharField(max_length=300)
    Uska_massage = models.TextField()

    def __str__(self):
        return f"Sabina ka massage {mainengine.Condition()}"
    def register(self):
        self.save()
        
    