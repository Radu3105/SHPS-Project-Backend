from rest_framework import serializers
from .models import Disease, Question, Symptom


class SymptomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symptom
        fields = ['id', 'name', 'question']


class DiseaseSerializer(serializers.ModelSerializer):
    symptoms = SymptomSerializer(many=True, read_only=True)

    class Meta:
        model = Disease
        fields = ['id', 'name', 'type', 'symptoms']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'text', 'symptom']
