# name = 'Niyi'
# age = 24
# weight = 105
# height = 1.75
# Goal = 'Lose weight'

# print(f"My name is {name}, I am {age} years old and I weigh {weight} kg.")

# method 1
# name = input("What is your name? ")
# print(f"hello", {name})

# age = int(input("What is your age? "))
# print(f"You are {age} years old.")

# weight = float(input("What is your weight in kg? "))
# print(f"You weigh {weight} kg.")

# height = float(input("What is your height in meters? "))    
# print(f"You are {height}, meters tall.")

# fitness_goal = input("What is your fitness goal? ")
# print(f"My fitness goal is {fitness_goal}")

user = [
        {
        "name": "Jude",
        "age": 12,
        "weight": 40,
        "height": 1.5,
        "fitness_goal": "Lose weight"
    },
    {
        "name": "David",
        "age": 28,
        "weight": 80,
        "height": 1.8,
        "fitness_goal": "Build muscle"
    },
    {
        "name": "Sarah",
        "age": 31,
        "weight": 65,
        "height": 1.6,
        "fitness_goal": "Improve fitness"
    }
]

workouts = [
            {
                "workout_name": "Bench Press",
                "target_muscle": "Chest",
                "difficulty": "Intermediate",
                "duration": 30,
                "exercises": ["Barbell Bench Press", "Dumbbell Bench Press", "Incline Bench Press"]
            },
            {
                "workout_name": "Squats",
                "target_muscle": "Legs",
                "difficulty": "Beginner",
                "duration": 45,
                "exercises": ["Bodyweight Squats", "Goblet Squats", "Barbell Back Squats"]
            },
            {
                "workout_name": "Deadlifts",
                "target_muscle": "Back",
                "difficulty": "Advanced",
                "duration": 60,
                "exercises": ["Conventional Deadlift", "Sumo Deadlift", "Romanian Deadlift"]
            }
]

for workout in workouts:
    print(f"Workout Name: {workout['workout_name']}")


def calculate_bmi(user):
    weight = user["weight"]
    height = user["height"]
    return weight / (height ** 2)

for person in user:
    bmi = calculate_bmi(person)
    print(f"{person['name']}'s BMI is {bmi}")

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return 'Healthy weight'
    elif bmi < 30:
        return 'Overweight'
    else:
        return 'Obese'
    
category = get_bmi_category(bmi)
print ("BMI category:", category)

def get_recommendation(category):
    if category == "Underweight":
        return "You should consider gaining weight through a balanced diet."
    elif category == "Healthy weight":
        return "Keep up the good work maintaining your weight!"
    elif category == "Overweight":
        return "Consider a healthy diet and regular exercise to lose weight."
    else:  # Obese
        return "It's important to consult with a healthcare provider for guidance on weight loss."
    
recommendation = get_recommendation(category)
print("Recommendation:", recommendation)