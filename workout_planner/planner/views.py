from django.shortcuts import render, redirect
from .forms import WorkoutRequestForm
from .models import WorkoutRequest
from .utils import generate_workout_routine

def create_workout_plan(request):
    if request.method == 'POST':
        form = WorkoutRequestForm(request.POST)
        if form.is_valid():
            workout_request = form.save(commit=False)
            
            # Generate the workout routine
            workout_request.generated_workout = generate_workout_routine(
                workout_request.fitness_level,
                workout_request.available_equipment,
                workout_request.workout_time,
                workout_request.goals
            )
            
            workout_request.save()
            return redirect('view_workout_plan', pk=workout_request.pk)
    else:
        form = WorkoutRequestForm()
    
    return render(request, 'planner/create_workout_plan.html', {'form': form})

def view_workout_plan(request, pk):
    workout_request = WorkoutRequest.objects.get(pk=pk)
    return render(request, 'planner/view_workout_plan.html', {'workout_request': workout_request})
