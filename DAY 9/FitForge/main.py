from models.user import FitnessUser
from models.workout import Workout
from services.tracker import FitnessTracker


user = FitnessUser(
    "Niyi",
    105,
    34,
    1.75,
    "Lose Weight"
)


tracker = FitnessTracker(user)


workout1 = Workout(
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
    30,
    300
)

workout5 = Workout(
    "Shoulder Day",
    40,
    320
)


tracker.add_workout(workout1)
tracker.add_workout(workout2)
tracker.add_workout(workout3)
tracker.add_workout(workout4)
tracker.add_workout(workout5)


user.display_profile()

tracker.show_history()

print(
    f"\nTotal calories burned: "
    f"{tracker.total_calories()}"
)

print(
    f"\nAverage Calories burned: "
    f"{tracker.average_calories()}"
)


longest = tracker.longest_workout()

if longest:
    print(
        f"Longest workout: "
        f"{longest.name} - "
        f"{longest.duration} minutes"
    )