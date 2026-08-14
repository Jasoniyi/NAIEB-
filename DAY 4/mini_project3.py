feedback = [
    {"user": "Jack", "rating": 5, "comment": "The app is amazing!"},
    {"user": "Sarah", "rating": 2, "comment": "The app is slow."},
    {"user": "David", "rating": 4, "comment": "Good workout recommendations."},
    {"user": "Alice", "rating": 1, "comment": "The app keeps crashing."},
    {"user": "Ben", "rating": 5, "comment": "I love the workout plans."},
]

total_rating = 0
average_rating = len(feedback)
count_positive_reviews = 0
count_negative_reviews = 0
negative_feedback = []
highest_rated_view = feedback[0]
number_of_rating = 0

for rating in feedback:
    total_rating += rating['rating']
    
    if rating['rating'] >= 4:
        count_positive_reviews += 1
        
    if rating['rating'] <=2:
        count_negative_reviews +=1
        negative_feedback.append(rating)
        
    if rating["rating"] > highest_rated_view["rating"]:
        highest_rated_view = rating
    
    
    
    
print(f"Average rating: {total_rating/average_rating}")
print(f"Positive Reviews: {count_positive_reviews}")
print(f"Negative Reviews: {count_negative_reviews}")

for negative_rating in negative_feedback:
    print(f"{negative_rating['user']} commented: {negative_rating['comment']}")

print(f"Highest Rated review: {highest_rated_view['rating']}")