from django.db import models
from teachers.models import Teacher


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    main_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    # assistant_teachers = models.ManyToManyField(Teacher)

    # Teacher는 나를 참고하고 있는 course_set을 그대로 주강의로 쓰고, M:N 관계에서는 assistant_courses라는 manager를 통해 받아옴
    assistant_teachers = models.ManyToManyField(Teacher, related_name="assistant_courses")
    # symmetrical 을 False로 설정하면 대칭 관계를 깨뜨릴 수 있음
    
    # 중개모델을 사용할 수도 있음 - 당연히 중개모델을 만들어줘야 함 - 얘는 순서 상관이 없나?
    # assistant_teachers = models.ManyToManyField(Teacher, related_name="assistant_courses", through='CourseInfo')


# 참조 : Through 참고 
# N:M 관계에서 추가적인 정보를 저장하고 싶은 경우에는 중개 모델을 사용할 수 있음
# 이 경우에는 중개 모델을 정의하고 through 옵션에 중개 모델을 지정하면 됨
# 중개모델에는 반드시 관계 설정을 원하는 두 모델을 ForeignKey로 지정해야 함
# class CourseInfo(models.Model):
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)  # Course 모델과의 관계
#     teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)  # Teacher 모델과의 관계
#     max_student = models.PositiveIntegerField(default=20)
#     is_nessary = models.BooleanField(default=False)
    
#     class Meta:
#         unique_together = ('course', 'teacher')
