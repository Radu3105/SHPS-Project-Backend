from django.db import models


class Symptom(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Specialization(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=[
                              ('M', 'Male'), ('F', 'Female')])
    date_of_birth = models.DateField()
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    specialization = models.ManyToManyField(
        Specialization, related_name='doctors', max_length=50)
    profile_picture = models.ImageField(blank=True)
    phone_number = models.CharField(max_length=12)
    email_address = models.EmailField()
    location_address = models.CharField(max_length=200)
    distance_to_location = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Disease(models.Model):
    name = models.CharField(max_length=50)
    doctor_specialization = models.ForeignKey(
        Specialization, related_name='diseases', on_delete=models.CASCADE)
    symptoms = models.ManyToManyField(Symptom, related_name='symptom')
    description = models.TextField(default="")
    prognosis_details = models.TextField(default="")
    treatement = models.TextField(default="")
    additional_resources = models.TextField(blank=True, default="")

    def __str__(self):
        return self.name
