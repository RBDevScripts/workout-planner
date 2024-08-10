from django.db import models

# Create your models here.

class WorkoutRequest(models.Model):
    fitness_level = models.CharField(max_length=50)
    available_equipment = models.TextField()
    workout_time = models.IntegerField(help_text="Preferred workout duration in minutes")
    goals = models.TextField(help_text="User's fitness goals")
    generated_workout = models.TextField(blank=True, null=True)
