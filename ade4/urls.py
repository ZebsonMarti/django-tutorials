from django.urls import path
from . import views

urlpatterns = [
    path("member_finance/", views.member_finance, name="create-member_finance"),
]
