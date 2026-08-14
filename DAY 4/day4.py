numbers = [12, 7, 25, 4, 18, 30, 9]

count = 0

for number in numbers:
   if number > 15:
         count += 1
         print(f"{number} is greater than 15.")

print(f"Total numbers greater than 15: {count}")

members = [
    {"name": "Niyi", "age": 34, "goal": "Lose weight"},
    {"name": "David", "age": 28, "goal": "Build muscle"},
    {"name": "Sarah", "age": 31, "goal": "Lose weight"},
    {"name": "John", "age": 40, "goal": "Maintain fitness"},
    {"name": "Emily", "age": 25, "goal": "Lose weight"},
]

count = 0
for member in members:
     if member['goal'] == "Lose weight":
         count += 1
         
print(f"Total members with the goal of losing weight: {count}")

workouts = [
    {"name": "Chest Day", "duration": 45, "calories": 350},
    {"name": "Leg Day", "duration": 60, "calories": 500},
    {"name": "Cardio", "duration": 30, "calories": 300},
    {"name": "Back Day", "duration": 50, "calories": 420},
]

total_workout_duration = 0
total_calories = 0
number_of_workouts = len(workouts)

for workout in workouts:
    total_workout_duration += workout['duration']
    total_calories += workout['calories']
    
average_workout_duration = total_workout_duration / number_of_workouts
average_calories = total_calories / number_of_workouts

print(f"Total workout duration: {total_workout_duration} minutes")
print(f"Average workout duration: {average_workout_duration} minutes")
print(f"Total calories burned: {total_calories} calories")
print(f"Average calories burned per workout: {average_calories} calories")

members = [
    {"name": "Niyi", "age": 34, "weight": 105},
    {"name": "David", "age": 28, "weight": 75},
    {"name": "Sarah", "age": 31, "weight": 65},
    {"name": "John", "age": 40, "weight": 85},
    {"name": "Michael", "age": 30, "weight": 95},
]

for member in members:
    # if member['weight'] > 80:
    #     print(f"{member['name']} weighs more than 80kg.")
    if member['name'] == "John":
        print(f"{member['name']} is {member['age']} years old, and weighs {member['weight']} kg")

members = [
    {"name": "Niyi", "age": 34},
    {"name": "David", "age": 28},
    {"name": "Sarah", "age": 31}
]

search_name = "David"

for member in members:
    if member["name"] == search_name:
        print(member)
        break
    
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number % 2 == 0:
        continue

    print(number)

users = [
    {"name": "Niyi", "active": True},
    {"name": "David", "active": False},
    {"name": "Sarah", "active": True},
    {"name": "John", "active": False},
]

for user in users:
    if not user["active"]:
        continue
    
    print(f"{user['name']} is active.")