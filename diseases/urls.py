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
    path('predict/', PredictDiseaseView.as_view(), name='predict_disease'),
    path('diseaseId/<str:disease_name>', GetDiseaseIdByName.as_view(), name='disease_id'),
    path('doctors/', DoctorsAPIView.as_view(), name='doctors'),
    path('doctors/<int:pk>', DoctorDetailAPIView.as_view(), name='doctor'),
    path('doctors/<str:specialization_name>', GetDoctorsBySpecialization.as_view(), name='doctors'), 
]
