# Mini Mission 2 - lists
food_list = ["Pizza", "Burger", "Pasta", "Salad", "Sushi"]

food_list.append("Eba")

print(food_list)

food_list.remove("Salad")
print(food_list)

food_list[3] = "Fufu"
print(food_list)

# Mini Mission 3 - dictionaries
user_profile = {
    "name": "Sam",
    "age": 25,
    "height": 6.2,
    "weight": 180,
    "fitness_goal": "Build Muscle",
    "favorite_exercise": "Bench Press"
}

print(user_profile["name"])
print(user_profile["height"])

user_profile["weight"] = 91

user_profile["Experience level"] = "Intermediate"

print(user_profile)

# Mini Mission 4 - lists of dictionaries
gym_members = [
    {
        "name": "Ben",
        "age": 34,
        "goal": "Lose weight",
        "experience_level": "Beginner"
    },
    {
        "name": "David",
        "age": 28,
        "goal": "Build muscle",
        "experience_level": "Intermediate"
    },
    {
        "name": "Sarah",
        "age": 31,
        "goal": "Improve fitness",
        "experience_level": "Advanced"
    }
]

for member in gym_members:
    print(f"{member['name']} - {member['goal']} - {member['experience_level']}")