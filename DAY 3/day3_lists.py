exercises = ["Bench Press", "squats", "Deadlift", "Pull-ups", "Push-ups"]

print(exercises[0])  
print(exercises[2]) 
print(exercises[-1]) 

exercises.append("Plank")

print(exercises)

exercises.remove("Push-ups")

print(exercises)

exercises[1] = "Lunges"

print(exercises)

users = [
    {
        "name": "Niyi",
        "age": 34,
        "goal": "Lose weight"
    },
    {
        "name": "David",
        "age": 28,
        "goal": "Build muscle"
    },
    {
        "name": "Sarah",
        "age": 31,
        "goal": "Improve fitness"
    }
]

for user in users:
    print(user["name"])
    
# Independence Practice Project
movie_watchlist = [
    {
        "title": "Inception",
        "genre": "Sci-Fi",
        "rating": 8.8,
        "year": 2010,
        "watched": True
    },
    {
        "title": "The Dark Knight",
        "genre": "Action",
        "rating": 9.0,
        "year": 2008,
        "watched": True
    },
    {
        "title": "Interstellar",
        "genre": "Sci-Fi",
        "rating": 8.6,
        "year": 2014,
        "watched": False
    },
    {
        "title": "The Matrix",
        "genre": "Sci-Fi",
        "rating": 8.7,
        "year": 1999,
        "watched": False
    },
    {
        "title": "The Shawshank Redemption",
        "genre": "Drama",
        "rating": 9.3,
        "year": 1994,
        "watched": True
    }
]

for movie in movie_watchlist:
    print(f"Print all movies:{movie['title']}")
    print("______________________________")
    if movie["watched"] == True:
        print(f"You have watched {movie['title']}.")
    print("______________________________")
    if movie["rating"] >+ 8:
        print(f"{movie['title']} is a great movie with a rating of {movie['rating']}.")
        
movie_watchlist.append({
    "title": "The Godfather",
    "genre": "Crime",
    "rating": 9.2,
    "year": 1972,
    "watched": True
})

print("______________________________")

# print(movie_watchlist["name"])

print("______________________________")

movie_watchlist[3]["watched"] = True
for movie in movie_watchlist:
    print(f"Print all movies status:{movie['watched']}")