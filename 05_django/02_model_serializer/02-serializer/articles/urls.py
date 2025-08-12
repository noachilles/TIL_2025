from django.urls import path
from . import views  

urlpatterns = [
    path('', views.article_get_or_create),
]