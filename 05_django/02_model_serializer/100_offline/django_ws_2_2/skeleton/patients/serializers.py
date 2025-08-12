from .models import Patient
from rest_framework import serializers

class PatientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('first_name', 'last_name', 'birth_date',)

class PatientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'