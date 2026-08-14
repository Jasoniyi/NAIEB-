#  DAY 3
# Gym Membership Console
gym_member = [
    {
        "name": "Ben",
        "age": 34,
        "weight": 80,
        "goal": "Lose weight",
        "membership_type": "Basic"
    },
    {
        "name": "David",
        "age": 28,
        "weight": 75,
        "goal": "Build muscle",
        "membership_type": "Premium"
    },
    {
        "name": "Sarah",
        "age": 31,
        "weight": 65,
        "goal": "Improve fitness",
        "membership_type": "Basic"
    },
    {
        "name": "John",
        "age": 40,
        "weight": 85,
        "goal": "Maintain fitness",
        "membership_type": "Premium"
    },
    {
        "name": "Emily",
        "age": 25,
        "weight": 55,
        "goal": "Lose weight",
        "membership_type": "Basic"
    },
    {
        "name": "Michael",
        "age": 30,
        "weight": 90,
        "goal": "Build muscle",
        "membership_type": "Premium"
    },
    {
        "name": "Jessica",
        "age": 27,
        "weight": 60,
        "goal": "Improve fitness",
        "membership_type": "Basic"
    },
    {
        "name": "Daniel",
        "age": 35,
        "weight": 95,
        "goal": "Maintain fitness",
        "membership_type": "Premium"
    },
]

workouts = [
    {
        "name": "Bench Press",
        "difficulty": "Intermediate",
        "duration": 30,
        "exercises": ["Barbell Bench Press", "Dumbbell Bench Press", "Incline Bench Press"]
    },
    {
        "name": "Squats",
        "difficulty": "Beginner",
        "duration": 45,
        "exercises": ["Bodyweight Squats", "Goblet Squats", "Barbell Back Squats"]
    },
    {
        "name": "Deadlifts",
        "difficulty": "Advanced",
        "duration": 60,
        "exercises": ["Conventional Deadlift", "Sumo Deadlift", "Romanian Deadlift"]
    }
]

# print("======== GYM MEMBERS ==========")
for member in gym_member:
    print(f"Name: {member['name']} | Age: {member['age']}, | Goal: {member['goal']} | Membership Type: {member['membership_type']}")
    if member['goal'] == "Build muscle":
        print(f"{member['name']} - {member['goal']}")

print("======== Available Workouts ==========")
for workout in workouts:
    print(f"Workout Name: {workout['name']} | Difficulty: {workout['difficulty']} | Duration: {workout['duration']} mins | Exercises: {', '.join(workout['exercises'])}")
    
print("======== CountMembership Type ==========")
premium_count = 0
basic_count = 0
get_member_age = 0

for member in gym_member:
    if member['membership_type'] == "Premium":
        premium_count += 1
    elif member['membership_type'] == "Basic":
        basic_count += 1
        
    get_member_age += member['age']
        
number_of_members = len(gym_member)
        
print(f"Premium Members: {premium_count}")
print(f"Basic Members: {basic_count}")
print(f"Total Members Age: {get_member_age}")
print(f"Average Age: {get_member_age/number_of_members}")

heaviest_member = gym_member[0]

for member in gym_member:
    if member['weight'] > heaviest_member['weight']:
        heaviest_member = member

print(f"Heaviest Member: {heaviest_member['name']} | Weight: {heaviest_member['weight']} kg")
