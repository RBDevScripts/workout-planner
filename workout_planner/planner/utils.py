from groq import Groq
from django.conf import settings

client = Groq(api_key="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")

def generate_workout_routine(fitness_level, equipment, workout_time, goals):
    promt = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "user",
                "content": f"create a workout plan with bullet points based on:\n\nFitness level: + {fitness_level} + \n\nAvailable equipment: + {equipment} +\n\nWorkout time:+ {workout_time} + \n(Preferred workout duration in minutes)\n\nGoals: + {goals} +\n(User's fitness goals). I am sending you this message through api and you response will be showed or website, so format the as needed to show best possible view"
            }
        ],
        
    )
    
    workout_plan = promt.choices[0].message.content
    return workout_plan
