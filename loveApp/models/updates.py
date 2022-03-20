from django.db import models

class Updates(models.Model):
    name = models.CharField(max_length=122)
    update = models.TextField()

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_updates():
        return Updates.objects.all()
    

    