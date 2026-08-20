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