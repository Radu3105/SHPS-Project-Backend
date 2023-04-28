from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Disease, Symptom
from .serializers import DiseaseSerializer, SymptomSerializer

# Create your views here.
class DiseaseAPIView(generics.ListCreateAPIView):
    serializer_class = DiseaseSerializer
    queryset = Disease.objects.all()


class DiseaseDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DiseaseSerializer
    queryset = Disease.objects.all()


class SymptomAPIView(generics.ListCreateAPIView):
    serializer_class = SymptomSerializer
    queryset = Symptom.objects.all()


class SymptomDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SymptomSerializer
    queryset = Symptom.objects.all()


class DiseaseSymptomsAPIView(generics.ListAPIView):
    serializer_class = SymptomSerializer

    def get_queryset(self):
        disease_id = self.kwargs['pk']
        disease = get_object_or_404(Disease, pk=disease_id)
        return disease.symptoms.all()
    