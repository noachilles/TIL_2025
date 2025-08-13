from rest_framework import serializers
from .models import Course
from teachers.serializers import TeacherSerializer


class CourseSerializer(serializers.ModelSerializer):
    '''
    강좌와 메인 강사는 1:N  관계
    강좌와 부강사는 M:N 관계
    '''
    # 사용자가 직접 입력하지 않아도 되는 필드이므로 read_only=True로 설정
    main_teacher = TeacherSerializer(read_only=True) 
    # 여러 명의 부강사를 나타내는 필드이므로 many=True로 설정
    assistant_teachers = TeacherSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'name', 'main_teacher', 'assistant_teachers')
