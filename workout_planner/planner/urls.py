from django.urls import path
from .views import create_workout_plan, view_workout_plan

urlpatterns = [
    path('', create_workout_plan, name='create_workout_plan'),  # This will be the home page
    path('workout/<int:pk>/', view_workout_plan, name='view_workout_plan'),
]
