from django.db import models

# Create your models here.
class Symptom(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Disease(models.Model):
    name = models.CharField(max_length=50)
    symptoms = models.ManyToManyField(Symptom, related_name='symptom')

    def __str__(self):
        return self.name
    