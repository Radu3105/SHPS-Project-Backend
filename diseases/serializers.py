from rest_framework import serializers
from .models import Disease, Doctor, Symptom, Specialization


class SymptomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symptom
        fields = ['id', 'name']


class DoctorSerializer(serializers.ModelSerializer):
    specialization_name = serializers.StringRelatedField(source='specialization.name')

    class Meta:
        model = Doctor
        fields = ['id', 'first_name', 'last_name', 'gender', 'date_of_birth', 'country', 'city', 'specialization', 'specialization_name', 'profile_picture', 'phone_number', 'email_address', 'location_address', 'geolocation']


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = ['id', 'name']


class DiseaseSerializer(serializers.ModelSerializer):
    symptoms = SymptomSerializer(many=True, read_only=True)
    doctor_specialization = SpecializationSerializer(read_only=True)

    class Meta:
        model = Disease
        fields = ['id', 'name', 'doctor_specialization', 'symptoms', 'description', 'prognosis_details', 'treatement', 'additional_resources']
