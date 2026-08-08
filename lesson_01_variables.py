# lesson_01_variables
# 1.
name = input("What is your name? ")
print("hello", name)

# 2.
age = int(input("What is your age? "))
print("You are", age, "years old.")

# 3.
weight = float(input("What is your weight in kg? "))
print("You weigh", weight, "kg.")

# 4.
height = float(input("What is your height in meters? "))    
print("You are", height, "meters tall.")

# 5.
FitnessGoal = input("What is your fitness goal? ")
print("My fitness goal is", FitnessGoal)

BMI = float(weight / (height ** 2))
print("My BMI is", BMI)