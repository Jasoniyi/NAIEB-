# Personal Expenses Tracker
expense = [
     {
         "description": "Groceries",
         "category": "Food",
         "amount": 150.75,
     },
     {
         "description": "Gas",
         "category": "Transport",
         "amount": 50.00
     },
     {
            "description": "Cinema",
            "category": "Entertainment",
            "amount": 75.25
     },
     {
         "description": "Internet Bill",
         "category": "Bills",
         "amount": 60.00
     },
     {
         "description": "Clothing",
         "category": "Shopping",
         "amount": 75.25
     },
     {
         "description": "Supermarket",
         "category": "Food",
         "amount": 350.75,
     },
 ]

total_spend = 0
food_spend = 0

for item in expense:
    total_spend += item["amount"]
    if item["category"] == "Food":
        food_spend += item["amount"]
        
    largest_expense = max(expense, key=lambda item: item["amount"])
    
print(f"the total spend is: {total_spend}")
print(f"the total spend on food is: {food_spend}")
print(f"the largest expense is: {largest_expense['description']} with an amount of {largest_expense['amount']}")

number_of_expenses = len(expense)
print(f"the number of expenses is: {number_of_expenses}")

    