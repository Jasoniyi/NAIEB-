# def greet_user():
#     print("Welcome to FitForge")
    
    
# greet_user()


# def show_profile(name, age, goal):
#    print(f"""=====PROFILE=======
#          Name: {name}
#          Age: {age}
#          Goal: {goal}
#          """) 
   
   
# show_profile("Ben", 27, "lose weight")

def log_workout(name, duration, calories, workout_type="strenght"):
      print(f"{name} comleted a {workout_type} training for {duration} minutes and burned {calories} calories")
      
details = log_workout("Ben", 45, 100)

print(details)

