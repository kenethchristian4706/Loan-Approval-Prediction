from django.urls import path
from . import views

urlpatterns = [
    path("", views.loan_form, name="loan_form"),
]
