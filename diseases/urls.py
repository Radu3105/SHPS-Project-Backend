from django.urls import path
from .views import *

urlpatterns = [
     path('diseases/', DiseaseAPIView.as_view(), name='diseases_list'),
     path('diseases/<int:pk>/', DiseaseDetailAPIView.as_view(), name='disease_detail'),
     path('diseases/<int:pk>/symptoms/',
          DiseaseSymptomsAPIView.as_view(), name='disease_symptoms'),
     path('symptoms/', SymptomAPIView.as_view(), name='symptoms_list'),
     path('symptoms/<int:pk>/', SymptomDetailAPIView.as_view(), name='symptom_detail'),
     path('symptoms/<int:pk>/diseases/',
          SymptomDiseasesAPIView.as_view(), name='symptom_diseases'),
     path('submit-data/', SubmitDataView.as_view(), name='submit_data'),
     path('diseases-by-symptoms/', DiseasesBySymptomsView.as_view(),
          name='diseases_by_symptoms'),
     path('question_by_symptom/<int:symptom_id>/', QuestionBySymptomView.as_view()),
]
