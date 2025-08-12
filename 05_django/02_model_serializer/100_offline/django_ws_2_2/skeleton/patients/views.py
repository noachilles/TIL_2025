from .models import Patient
from .serializers import PatientListSerializer, PatientCreateSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(["POST", "GET"])
def patient_create(request):
    if request.method == 'POST':
        serializer = PatientCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    elif request.method == 'GET':
        # Patient에 있는 모든 요소
        patients = Patient.objects.all()
        # serializer 만들어서, 반환
        serializer = PatientListSerializer(patients, many=True)
        return Response(serializer.data, status=201)