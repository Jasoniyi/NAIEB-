weekly_workouts = [
    {"day": "Monday", "type": "Strength", "duration": 50, "calories": 400},
    {"day": "Tuesday", "type": "Cardio", "duration": 35, "calories": 320},
    {"day": "Wednesday", "type": "Strength", "duration": 60, "calories": 480},
    {"day": "Thursday", "type": "Rest", "duration": 0, "calories": 0},
    {"day": "Friday", "type": "Cardio", "duration": 45, "calories": 390},
    {"day": "Saturday", "type": "Strength", "duration": 70, "calories": 550},
    {"day": "Sunday", "type": "Rest", "duration": 0, "calories": 0},
]

print("===== WEEKLY FITNESS REPORT =====")



rest_days = 0
total_workout_time = 0
total_calories_burned = 0
most_intense_workout = weekly_workouts[0]

for workout in weekly_workouts:
    if workout['duration'] == 0:
        rest_days += 1
        
    total_workout_time += workout["duration"]
    
    total_calories_burned += workout['calories']
    
    if workout["calories"] > most_intense_workout['calories']:
        most_intense_workout = workout
        
        
workout_days = len(weekly_workouts) - rest_days
average_duration = total_workout_time / workout_days
average_calories = total_calories_burned / workout_days

print(f"Workout days: {workout_days}")        
print(f"rest days: {rest_days}")
print(f"Total workout time: {total_workout_time} minutes")
print(f"Total calories burned: {total_calories_burned}")
print(f"Average workout duration: {average_duration} minutes")
print(f"Average calories burned: {average_calories}")
print(f"Most intense workout: {most_intense_workout['day']} - {most_intense_workout['type']} - {most_intense_workout['calories']}")
    