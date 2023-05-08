from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Disease, Symptom
from .serializers import DiseaseSerializer, SymptomSerializer


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


class SymptomDiseasesAPIView(generics.ListAPIView):
    serializer_class = DiseaseSerializer

    def get_queryset(self):
        symptom_id = self.kwargs['pk']
        symptom = Symptom.objects.get(name=symptom_id)
        return symptom.diseases.all()


class DiseasesBySymptomsView(APIView):
    def post(self, request):
        symptoms = request.data.get("symptoms", [])

        # Get all diseases that have the specified symptoms
        query = Q()
        for symptom in symptoms:
            query |= Q(symptoms__name__iexact=symptom)

        diseases = Disease.objects.filter(query).distinct()

        # Serialize the diseases
        disease_serializer = DiseaseSerializer(diseases, many=True)

        return Response({"status": "success", "data": disease_serializer.data})


class SubmitDataView(APIView):
    def post(self, request):
        symptoms = request.data.get("symptoms")

        return Response(symptoms)
