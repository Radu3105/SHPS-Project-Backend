# Generated by Django 4.0.1 on 2023-07-30 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=1)),
                ('age', models.IntegerField()),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('profile_picture', models.ImageField(upload_to='')),
                ('phone_number', models.CharField(max_length=12)),
                ('email_address', models.EmailField(max_length=254)),
                ('location_address', models.CharField(max_length=200)),
                ('distance_to_location', models.IntegerField()),
                ('specialization', models.ManyToManyField(max_length=50, related_name='doctors', to='diseases.Specialization')),
            ],
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('doctor_specialization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diseases', to='diseases.specialization')),
                ('symptoms', models.ManyToManyField(related_name='symptom', to='diseases.Symptom')),
            ],
        ),
    ]
