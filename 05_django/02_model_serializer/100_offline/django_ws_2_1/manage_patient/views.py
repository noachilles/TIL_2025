from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import PatientSerializer

# Create your views here.
@api_view(['POST'])
def new_patient(request):
    # serializer가 필요함
    serializer = PatientSerializer(data=request.data)
    # 정보가 유효한지 검증
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        # 정상: 저장
        return Response(serializer.data)