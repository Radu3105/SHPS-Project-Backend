from django.contrib import admin
from .models import Disease, Symptom, DiseaseType, Specialization, Doctor

# Register your models here.
admin.site.register(Symptom)
admin.site.register(DiseaseType)
admin.site.register(Disease)
admin.site.register(Specialization)
admin.site.register(Doctor)
