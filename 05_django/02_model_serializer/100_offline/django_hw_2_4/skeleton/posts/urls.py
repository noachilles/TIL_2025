from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.create_read_post),
    path("<int:post_pk>/", views.update_delete_post),
]
