# Generated by Django 4.0.1 on 2023-07-30 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diseases', '0002_alter_doctor_age_alter_doctor_profile_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='age',
            new_name='date_of_birth',
        ),
    ]
