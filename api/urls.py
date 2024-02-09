from django.urls import path
from api import api_views

urlpatterns = [path("salaries", api_views.SalaryAPIView.as_view(), name="salaries"),
               path("salaries/<int:pk>", api_views.SalaryAPIView.as_view(), name="salaries_with_pk")
               ]
