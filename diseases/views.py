from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Disease, Question, Symptom
from .serializers import DiseaseSerializer, QuestionSerializer, SymptomSerializer
from rest_framework import status


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

##################################################################################################


class DiseasesBySymptomsView(APIView):
    def post(self, request):
        symptoms = request.data.get("symptoms", [])
        symptoms_ids = []
        for symptom in symptoms:
            symptoms_ids.append(symptom['id'])
        diseases = Disease.objects.filter(symptoms__in=symptoms_ids).distinct()
        disease_serializer = DiseaseSerializer(diseases, many=True)

        for disease in diseases:
            print(disease.symptoms.all())

        return Response()
    
##################################################################################################

    def get(self, request):
        symptomDiseases = Symptom.diseases.all()
        serializer = DiseaseSerializer(symptomDiseases, many=True)
        return Response({"data": symptomDiseases.data})


class SymptomDiseasesAPIView(generics.ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        symptom_id = self.kwargs['pk']
        question = Question.objects.get(name=symptom_id)
        return question.symptom


class QuestionBySymptomView(APIView):
    def get(self, request, symptom_id):
        try:
            symptom = Symptom.objects.get(id=symptom_id)
            print(type(symptom))
        except Symptom.DoesNotExist:
            return Response({'error': 'Symptom does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            question = symptom.question
        except Question.DoesNotExist:
            return Response({'error': 'No question associated with this symptom.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = QuestionSerializer(question)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SubmitDataView(APIView):
    def post(self, request):
        symptoms = request.data.get("symptoms")
        return Response(symptoms)


