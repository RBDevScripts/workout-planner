from django import forms
from .models import WorkoutRequest

class WorkoutRequestForm(forms.ModelForm):
    class Meta:
        model = WorkoutRequest
        fields = ['fitness_level', 'available_equipment', 'workout_time', 'goals']
