workout_history = [
    {
        "user": "Jack",
        "workout": "Upper Body",
        "duration": 45,
        "calories": 320
    },
    {
        "user": "Ben",
        "workout": "Leg Day",
        "duration": 55,
        "calories": 410
    },
    {
        "user": "Bill",
        "workout": "Cardio",
        "duration": 30,
        "calories": 250
    },
    {
        "user": "Alice",
        "workout": "Upper Body",
        "duration": 50,
        "calories": 350
    }
]

total_duration = 0
total_calories = 0
highest_workout = workout_history[0]
longest_workout = workout_history[0]
total_workouts = len(workout_history)
highest_calories = workout_history[0]
longest_workout = workout_history[0]

print("===== FITNESS ANALYTICS =====")
print (f"Total wokouts: {total_workouts}")

for workout in workout_history:
    total_duration += workout['duration']
    total_calories += workout['calories']
    
print(f"Total workout duration: {total_duration} minutes")
print(f"Total calories burned: {total_calories} calories")
print(f"Average calories: {total_calories / total_workouts}")

for workout in workout_history:
    if workout['calories'] > highest_calories['calories']:
        highest_calories = workout
        
    if workout['duration'] > longest_workout['duration']:
        longest_workout = workout
        
print(f"Highest calories burned in a workout: {highest_calories['workout']} - {highest_calories['calories']}")

print(f"Longest workout duration: {longest_workout['workout']} - {longest_workout['duration']} minutes")