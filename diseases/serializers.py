from rest_framework import serializers
from .models import Disease, Symptom


class SymptomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symptom
        fields = ['id', 'name']


class DiseaseSerializer(serializers.ModelSerializer):
    symptoms = SymptomSerializer(many=True, read_only=True)

    class Meta:
        model = Disease
        fields = ['id', 'name', 'type', 'symptoms']
