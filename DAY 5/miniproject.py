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

def calculate_total_duration(workout):
    total_duration = 0
    
    for workout in workout_history:
        total_duration += workout['duration']
        
    return total_duration
        

def calculate_total_calories(workout):
    total_calories = 0
    
    for workout in workout_history:
        total_calories += workout['calories']
        
    return total_calories

number_of_workout = len(workout_history)

def calculate_average_duration(workout):
    average_duration = calculate_total_duration(workout_history) / number_of_workout
    
    return average_duration
    

print("===== FITNESS ANALYTICS =====")

print(f"Total duration: {calculate_total_duration(workout_history)} minutes")

print(f"Total calories: {calculate_total_calories(workout_history)}")

print(f"Average calories: {calculate_average_duration(workout_history)}")