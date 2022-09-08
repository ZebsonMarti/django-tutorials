from django.urls import path
from . import views

urlpatterns = [
    path("upload/", views.ProcessImageView.as_view(), name="process_image"),
    path("image-list/", views.ImageListView.as_view(), name="image_list"),
]
