from django import forms
from django.contrib import admin
from .models import Disease, Symptom, Doctor, Specialization


admin.site.register(Symptom)
admin.site.register(Doctor)
admin.site.register(Disease)
admin.site.register(Specialization)
