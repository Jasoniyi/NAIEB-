from models.workout import Workout

class FitnessTracker:

    def __init__(self, user):
        self.user = user
        self.workouts = []

    def add_workout(self, workout):
        self.workouts.append(workout)

    def show_history(self):

        print(
            f"\n===== "
            f"{self.user.name.upper()}'S WORKOUT HISTORY ====="
        )

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

        if not self.workouts:
            return None

        longest = self.workouts[0]

        for workout in self.workouts:
            if workout.duration > longest.duration:
                longest = workout

        return longest
    
    def average_calories(self):
        
        if not self.workouts:
            return None
        
        number_of_workouts = len(self.workouts)
        
        return self.total_calories() / number_of_workouts
            