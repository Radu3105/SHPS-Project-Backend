from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Disease, Symptom, Doctor
from .serializers import DiseaseSerializer, SymptomSerializer, DoctorSerializer, SpecializationSerializer
from django.core.exceptions import ObjectDoesNotExist
import joblib


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


# class QuestionAPIView(generics.ListCreateAPIView):
#     serializer_class = QuestionSerializer
#     queryset = Question.objects.all()


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


# class DiseasesBySymptomsView(APIView):
#     def post(self, request):
#         symptoms = request.data.get("symptoms", [])
#         symptoms_ids = []
#         for symptom in symptoms:
#             symptoms_ids.append(symptom['id'])
#         diseases = Disease.objects.filter(symptoms__in=symptoms_ids).distinct()
#         questions = []
#         for disease in diseases:
#             for symptom in disease.symptoms.all():
#                 try:
#                     questions.append(symptom.question)
#                 except ObjectDoesNotExist:
#                     print("This symptom has no associated question.")
        # question_serializer = QuestionSerializer(questions, many=True)

        # return Response(question_serializer.data[random.randint(0, len(question_serializer.data) - 1)])


####################################################################################################


# class QuestionView(APIView):
#     def get(self, request, question_id):
#         try:
#             question = Question.objects.get(id=question_id)
#         except Question.DoesNotExist:
#             raise Http404

#         serializer = QuestionSerializer(question)
#         return Response(serializer.data)


# class SymptomDiseasesAPIView(generics.ListAPIView):
#     serializer_class = QuestionSerializer

#     def get_queryset(self):
#         symptom_id = self.kwargs['pk']
#         question = Question.objects.get(name=symptom_id)
#         return question.symptom


# class QuestionBySymptomView(APIView):
#     def get(self, request, symptom_id):
#         try:
#             symptom = Symptom.objects.get(id=symptom_id)
#             print(type(symptom))
#         except Symptom.DoesNotExist:
#             return Response({'error': 'Symptom does not exist.'}, status=status.HTTP_404_NOT_FOUND)

#         try:
#             question = symptom.question
#         except Question.DoesNotExist:
#             return Response({'error': 'No question associated with this symptom.'}, status=status.HTTP_404_NOT_FOUND)

#         serializer = QuestionSerializer(question)
#         return Response(serializer.data, status=status.HTTP_200_OK)


class SubmitDataView(APIView):
    def post(self, request):
        symptoms = request.data.get("symptoms")
        return Response(symptoms)


class PredictDiseaseView(APIView):
    def post(self, request):
        model = joblib.load('./training/decision_tree_model.pkl')
        selected_symptoms = request.data.get("symptoms")
        all_symptoms = Symptom.objects.all()
        symptom_serializer = SymptomSerializer(all_symptoms, many=True)
        list_of_symptoms = []
        # potential_diseases = []
        for symptom in symptom_serializer.data:
            list_of_symptoms.append(symptom['name'])
        indices = []
        for selected_symptom in selected_symptoms:
            for i in range(len(list_of_symptoms)):
                if selected_symptom['name'] == list_of_symptoms[i]:
                    indices.append(i)
        data = [[]]
        for i in range(132):
            data[0].append(0)
        for i in range(len(indices)):
            data[0][indices[i]] = 1
        y_pred = model.predict(data)
        return Response({'result': y_pred})


class GetDiseaseIdByName(APIView):
    def get(self, request, disease_name):
        try:
            disease = Disease.objects.get(name=disease_name)
            disease_id = disease.id
            return Response({'id': disease_id})
        except ObjectDoesNotExist:
            return Response("No object matches that name!")


class DoctorsAPIView(generics.ListCreateAPIView):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()


class DoctorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()


class GetDoctorsBySpecialization(APIView):
    def get(self, request, specialization_name, *args, **kwargs):
        try:
            doctors = Doctor.objects.filter(
                specialization__name=specialization_name)
            if not doctors:
                return Response("No doctor matches that specialization!")
            doctor_serializer = DoctorSerializer(doctors, many=True)
            # specialization_serializer = SpecializationSerializer()
            # print(serializer.data)
            return Response(doctor_serializer.data)
        except ObjectDoesNotExist:
            return Response("No doctor matches that specialization!")
        
        
class GetSpecializationById(APIView):
    def get(self, request):
        try:
            pass
        except ObjectDoesNotExist:
            return Response("No specialization matches that id!")
