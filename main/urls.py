from django.urls import path
from .views import attendance_view

urlpatterns = [
    path('',attendance_view, name="attendance_view")
]