members = [
    {
        "name": "Niyi",
        "age": 34,
        "weight": 105,
        "goal": "Lose weight"
    },
    {
        "name": "David",
        "age": 28,
        "weight": 75,
        "goal": "Build muscle"
    },
    {
        "name": "Sarah",
        "age": 31,
        "weight": 65,
        "goal": "Lose weight"
    },
    {
        "name": "John",
        "age": 40,
        "weight": 85,
        "goal": "Maintain fitness"
    }
]



def find_member(members, name):
    for member in members:
        if name == member['name']:
            return member
        
print(f"Member is: {find_member(members, "Sarah")}")

def count_members_by_goal(members, goal):
    count_member = 0
    
    for member in members:
        if goal == member['goal']:
            count_member += 1
            
    return count_member

print(f"members with same goal is {count_members_by_goal(members, "Lose weight")}")

def find_heaviest_member(members):
    heaviest_member = members[0]
    
    for member in members:
        if member['weight'] > heaviest_member['weight']:
            heaviest_member = member
            
    return heaviest_member

print(f"heaviest member is {find_heaviest_member(members)}")

def generate_member_summary(member):
    return f"""
===== MEMBER SUMMARY =====
Name: {member['name']}
Age: {member['age']}
Weight: {member['weight']} kg
Goal: {member['goal']}
==========================
"""


print(generate_member_summary(members[0]))