# name = 'Niyi'
# age = 24
# weight = 105
# height = 1.75
# Goal = 'Lose weight'

# print(f"My name is {name}, I am {age} years old and I weigh {weight} kg.")

name = input("What is your name? ")
print("hello", name)

age = int(input("What is your age? "))
print("You are", age, "years old.")

weight = float(input("What is your weight in kg? "))
print("You weigh", weight, "kg.")

height = float(input("What is your height in meters? "))    
print("You are", height, "meters tall.")

FitnessGoal = input("What is your fitness goal? ")
print("My fitness goal is", FitnessGoal)


def calculate_bmi(weight, height):
    return weight / (height ** 2)

BMI = calculate_bmi(weight, height)

print("My BMI is", BMI)

def get_bmi_category(BMI):
    if BMI < 18.5:
        return "Underweight"
    elif BMI < 25:
        return 'Healthy weight'
    elif BMI < 30:
        return 'Overweight'
    else:
        return 'Obese'
    
category = get_bmi_category(BMI)
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