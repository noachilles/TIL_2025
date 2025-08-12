from .models import Patient
from .serializers import PatientSerializer, PatientListSerializer, PatientSearchSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
@api_view(["POST"])
def patient_create(request):
    serializer = PatientSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=201)
    

@api_view(['GET'])
def patient_list(request):
    patients = Patient.objects.all()
    serializer = PatientListSerializer(patients, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def patient_search(request, patient_pk):
    try:
        patient = Patient.objects.get(id=patient_pk) # get이 아니라 filter로 하면 error 발생 이유는?
        serializer = PatientSearchSerializer(patient)
        return Response(serializer.data)
    except ObjectDoesNotExist:
            return Response({"detail": "No Patient matches the given query."})
    
        