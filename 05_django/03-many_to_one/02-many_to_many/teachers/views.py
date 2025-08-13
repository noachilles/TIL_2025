from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Teacher
from .serializers import TeacherSerializer


@api_view(["GET", "POST"])
def teachers(request):
    if request.method == "GET":
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)

    if request.method == "GET":
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == "DELETE":
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        