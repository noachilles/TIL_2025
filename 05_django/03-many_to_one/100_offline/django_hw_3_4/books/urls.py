from django.urls import path
from . import views

urlpatterns = [
    path("<int:genre_pk>/", views.genre_detail)
]
