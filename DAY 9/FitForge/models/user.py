from utils.calculations import calculate_bmi

class FitnessUser:

    def __init__(self, name, weight, age, height, goal):
        self.name = name
        self.weight = weight
        self.age = age
        self.height = height
        self.goal = goal

    def introduce(self):
        print(
            f"My name is {self.name} "
            f"and I weigh {self.weight} kg"
        )

    def get_bmi_category(self):
        bmi = calculate_bmi(self.weight, self.height)

        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Healthy weight"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese"

    def display_profile(self):
        bmi = calculate_bmi(self.weight, self.height)
        category = self.get_bmi_category()

        print("\n===== FITNESS PROFILE =====")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Weight: {self.weight} kg")
        print(f"Height: {self.height} m")
        print(f"Goal: {self.goal}")
        print(f"BMI: {bmi:.1f}")
        print(f"Category: {category}")
        print("===========================")