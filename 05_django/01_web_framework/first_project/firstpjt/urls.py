"""
URL configuration for firstpjt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include   # include 사용 - 여러 개의 app 사용을 위해
# articles app이 가지고 있는 views 모듈  
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('articles/', include('articles.urls'))

    # 사용자가 index라는 경로로 요청을 보내면?
    # views에 있는 index 함수를 실행시킨다.
    # 마지막 slash 반드시 붙이기
    # path('index/', views.index),
    
    # variable routing
    # 경로에 사용자가 적은 값을 변수에 담고싶어
        # <variable_name>
    # path('article/<variable_name>/', views.detail),
        # <int:variable_name>: 정수만 허용
    # path('article/<int:variable_name>/', views.detail),
    
    # path('article/<int:article_pk>/', views.detail),
    # 동작하도록 하려면 detail 함수를 정의할 때 입력받은 article_pk 라는 변수를 그대로 가져가 사용

    # 기능이 많으면 -> 경로가 여러 개일 수밖에 없음
    # => 여러 개의 앱을 사용하고, 경로도 여러 개 만드는 수밖에 없음
    # PJT가 커지면 -> app마다 경로 따로 관리  
    # include라는 기능을 사용

]
