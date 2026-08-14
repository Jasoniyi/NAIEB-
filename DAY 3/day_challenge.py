# Day 3
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


total_calories = 0
total_duration = 0
highest_workout = workout_history[0]

number_of_workouts = len(workout_history)

for history in workout_history:
    total_calories += history['calories']
    total_duration += history['duration']
    if history['calories'] > highest_workout["calories"]:
        highest_workout = history

print("===== WORKOUT SUMMARY =====")

print(f"Number of Workouts: {number_of_workouts}")
print(f"Total workout time: {total_duration} mins")
print(f"Total Calories burned: {total_calories}")
print(f"Average Calories: {total_calories/number_of_workouts}")
print(
    f"Best calorie-burning workout: "
    f"{highest_workout['workout']} - "
    f"{highest_workout['calories']} calories"
)