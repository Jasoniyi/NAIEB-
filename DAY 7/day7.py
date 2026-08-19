# class User:
#     def __init__(self, name, age, weight):
#         self.name = name
#         self.age = age
#         self.weight = weight

# user1 = User("Sam", 34, 105)

# print(user1.name)

class FitnessUser:
    def __init__(self, name, weight, age, height, goal):
        self.name = name
        self.weight = weight
        self.height = height
        self.goal = goal
        self.age = age
        
    def introduce(self):
        print(f"My name is {self.name} and i weigh {self.weight} kg")
        
    def calculate_bmi(self):
        bmi = self.weight / (self.height * self.height)
        return bmi
    
    def get_bmi_category(self):
        bmi = self.calculate_bmi()

        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Healthy weight"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese"
    
    def display_profile(self):
        bmi = self.calculate_bmi()
        bmi_category = self.get_bmi_category()
        
        print("\n===== FITNESS PROFILE =====")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Weight: {self.weight} kg")
        print(f"Height: {self.height} m")
        print(f"Goal: {self.goal}")
        print(f"BMI: {bmi:.1f}")
        print(f"Category: {bmi_category}")
        print("===========================")
        
        
class Workout:
    def __init__(self, name, duration, calories):
        self.name = name
        self.duration = duration
        self.calories = calories
        
    def display_workout(self):
        print(
            f"Workout: {self.name} | "
            f"Duration: {self.duration} minutes | "
            f"Calories: {self.calories}"
        )
        
class FitnessTracker:
    def __init__(self, user):
        self.user = user
        self.workouts = []
        
    def add_workout(self, workout):
        self.workouts.append(workout)
        
    def show_history(self):
        print(f"\n===== {self.user.name}'S WORKOUT HISTORY =====")
        
        if not self.workouts:
            print("No workouts recorded yet.")
            return
        
        for workout in self.workouts:
            workout.display_workout()
            
    def total_calories(self):
        total = 0
        
        for workout in self.workouts:
            total += workout.calories
            
        return total
    
    def longest_workout(self):
        longest_workout = self.workouts[0]
        
        for workout in self.workouts:
            if workout.duration > longest_workout.duration:
                longest_workout = workout
                
        return longest_workout
    
    # Create a user
user = FitnessUser(
    "Niyi",
    34,
    105,
    1.75,
    "Lose Weight"
)

# Create a fitness tracker for the user
tracker = FitnessTracker(user)

# Create a workout
workout = Workout(
    "Leg Day",
    60,
    500
)

workout2 = Workout(
    "Chest Day",
    45,
    350
)

workout3 = Workout(
    "Back Day",
    50,
    400
)

workout4 = Workout(
    "Running",
    90,
    300
)

workout5 = Workout(
    "Shoulder Day",
    40,
    320
)

# Add workout to tracker
tracker.add_workout(workout)
tracker.add_workout(workout2)
tracker.add_workout(workout3)
tracker.add_workout(workout4)
tracker.add_workout(workout5)

# Display user profile
user.display_profile()

# Display workout history
tracker.show_history()

# Display total calories
print(f"\nTotal calories burned: {tracker.total_calories()}")

# Display longest workout
longest = tracker.longest_workout()
print(f"Longest workout: {longest.name}")
print(f"Duration: {longest.duration} minutes")