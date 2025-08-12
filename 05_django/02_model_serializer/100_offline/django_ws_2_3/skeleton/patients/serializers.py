from .models import Patient
from rest_framework import serializers

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class PatientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('first_name', 'last_name', 'birth_date',)

class PatientSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        exclude = ('created_at',)