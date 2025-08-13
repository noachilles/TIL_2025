from django.urls import path
from . import views

urlpatterns = [
    path('<int:author_id>/', views.author_detail),
]