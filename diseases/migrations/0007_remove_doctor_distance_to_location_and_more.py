# Generated by Django 4.0.1 on 2023-09-08 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diseases', '0006_alter_disease_additional_resources_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='distance_to_location',
        ),
        migrations.AddField(
            model_name='doctor',
            name='geolocation',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
