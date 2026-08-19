def get_valid_name():
    while True:
        name = input("Enter your name: ").strip()

        if name:
            return name

        print("Name cannot be empty. Please try again.")


def get_valid_age():
    while True:
        try:
            age = int(input("Enter your age: "))

            if 1 <= age <= 120:
                return age

            print("Age must be between 1 and 120.")

        except ValueError:
            print("Please enter a valid number.")


def get_valid_weight():
    while True:
        try:
            weight = float(input("Enter your weight in kg: "))

            if weight > 0:
                return weight

            print("Weight must be greater than zero.")

        except ValueError:
            print("Please enter a valid number.")


def get_valid_height():
    while True:
        try:
            height = float(input("Enter your height in meters: "))

            if height > 0:
                return height

            print("Height must be greater than zero.")

        except ValueError:
            print("Please enter a valid number.")


def calculate_bmi(weight, height):
    return weight / (height ** 2)


def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def display_profile(name, age, weight, height, bmi, category):
    print("\n===== FITFORGE PROFILE =====")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Weight: {weight:.1f} kg")
    print(f"Height: {height:.2f} m")
    print(f"BMI: {bmi:.1f}")
    print(f"BMI Category: {category}")
    print("============================")


# Get user information
name = get_valid_name()
age = get_valid_age()
weight = get_valid_weight()
height = get_valid_height()

# Calculate BMI
bmi = calculate_bmi(weight, height)

# Determine BMI category
category = get_bmi_category(bmi)

# Display profile
display_profile(name, age, weight, height, bmi, category)