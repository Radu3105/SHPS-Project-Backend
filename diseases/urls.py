from django.urls import path
from .views import DiseaseAPIView, DiseaseDetailAPIView, DiseaseSymptomsAPIView, SymptomAPIView, SymptomDetailAPIView

urlpatterns = [
    path('diseases/', DiseaseAPIView.as_view(), name='diseases_list'),
    path('diseases/<int:pk>/', DiseaseDetailAPIView.as_view(), name='disease_detail'),
    path('diseases/<int:pk>/symptoms/', DiseaseSymptomsAPIView.as_view(), name='disease_symptoms'),
    path('symptoms/', SymptomAPIView.as_view(), name='symptoms_list'),
    path('symptoms/<int:pk>/', SymptomDetailAPIView.as_view(), name='symptom_detail'),
]