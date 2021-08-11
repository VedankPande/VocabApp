from django.db import models
import random


class Words(models.Model):
    word = models.CharField(max_length=40)
    meaning = models.CharField(max_length=300)

    def next(self):
        try:
            return Words.objects.filter(id=self.id+1).first()
        except:
            return None

    def prev(self):
        try:
            if id!=1:
                return Words.objects.filter(id=self.id-1).first()
        except:
            return None

    def random(self):
        id = random.randint(1,262)
        try:
            return Words.objects.filter(id=id).first()
        except:
            return None
