from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Course
from teachers.models import Teacher
from .serializers import CourseSerializer

# Create your views here.

# 메인 강사 pk를 받아서 새로운 강좌를 생성
@api_view(["POST"])
def create_course(request, teacher_pk):
    teacher = get_object_or_404(Teacher, pk=teacher_pk)
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(main_teacher=teacher)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

@api_view(["GET", "PUT", "DELETE"])
def course(request, course_pk):
    course = get_object_or_404(Course, pk=course_pk)
    if request.method == "GET":
        serializer = CourseSerializer(course)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
def assistant(request, course_pk, teacher_pk):
    '''
    path parameter로 받은 course_pk와 teacher_pk를 이용해 해당 강좌에 참여할 부강사를 지정
    이미 부강사로 지정되어 있는 경우에는 해당 강좌 부강사에서 제외
    부강사 지정/해제 후 강좌 정보를 반환
    M:N 관계에서는 add()와 remove() 메서드를 사용해 중개 모델을 통해 관계를 생성/해제
    '''
    # get 했는데, 있으면 해당 data, 없으면 404 error
    course = get_object_or_404(Course, pk=course_pk) # course_pk에 해당하는 Course 객체를 가져옴
    teacher = get_object_or_404(Teacher, pk=teacher_pk) # teacher_pk에 해당하는 Teacher 객체를 가져옴
    if teacher in course.assistant_teachers.all(): # 이미 부강사로 지정되어 있는 경우
        course.assistant_teachers.remove(teacher) # 해당 강좌의 부강사에서 제외
    else: # 부강사로 지정되어 있지 않은 경우
        course.assistant_teachers.add(teacher) # 해당 강좌의 부강사로 지정
    return Response(CourseSerializer(course).data, status=status.HTTP_200_OK)
    
