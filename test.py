import os
import django
import string

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'shps.settings')
django.setup()

from diseases.models import Symptom, Disease, Specialization  # Replace with your actual app's name
import sys
sys.path.append('/path/to/training')

# from training.training import symptoms
import pandas as pd

df = pd.read_csv("./training/Training.csv")
df = df.drop(["Unnamed: 133"],axis=1)

diseases = list(set(df['prognosis'].values))
symptoms = list(df.columns)
symptoms.remove('prognosis')
# print(diseases)

def populate_db_symptoms():
    for i in range(len(symptoms)):
        _loc = symptoms[i].find('_')
        if _loc != -1:
            symptoms[i] = symptoms[i].replace('_', ' ')
        symptoms[i] = symptoms[i].capitalize()

        Symptom.objects.create(name=symptoms[i])


# !! For populating diseases with symptoms look on google for symptoms for each disease in here:
def populate_db_diseases():
    s, created = Specialization.objects.get_or_create(name="Cardiologist")
    for d in diseases:
        Disease.objects.create(name=d, doctor_specialization=s)


# Uncomment to populate different db models
# ==========================================

# populate_db_symptoms()
populate_db_diseases()
