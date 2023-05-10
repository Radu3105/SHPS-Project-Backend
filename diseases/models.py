from django.db import models

# Create your models here.


class Symptom(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Question(models.Model):
    text = models.TextField()
    symptom = models.OneToOneField(Symptom, on_delete=models.CASCADE, related_name='question')

    def __str__(self):
        return self.text

class DiseaseType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Disease(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey(DiseaseType, on_delete=models.CASCADE)
    symptoms = models.ManyToManyField(Symptom, related_name='symptom')

    def __str__(self):
        return self.name


class Specialization(models.Model):
    name = models.CharField(max_length=50)
    disease_type = models.ForeignKey(DiseaseType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    specialization_id = models.ForeignKey(
        Specialization, on_delete=models.CASCADE)
    disease_type = models.ManyToManyField(
        DiseaseType, related_name="disease_type")

    def __str__(self):
        return self.name
