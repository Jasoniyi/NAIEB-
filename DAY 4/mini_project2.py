expenses = [
    {"description": "Groceries", "category": "Food", "amount": 45000},
    {"description": "Uber", "category": "Transport", "amount": 12000},
    {"description": "Netflix", "category": "Entertainment", "amount": 5000},
    {"description": "Electricity", "category": "Bills", "amount": 25000},
    {"description": "Restaurant", "category": "Food", "amount": 18000},
    {"description": "Fuel", "category": "Transport", "amount": 20000},
    {"description": "Shoes", "category": "Shopping", "amount": 35000},
]

total_spending = 0
food_spending = 0
transport_spending = 0
number_of_expenses = len(expenses)
largest_expense = expenses[0]
average_expense = 0
expenses_above_20000 = []

print("====EXPENSE ANALYZER====")
for expense in expenses:
    total_spending += expense['amount']
    
    
    if expense['category'] == "Food":
        food_spending += expense['amount']
        
        
    if expense["category"] =="Transport":
        transport_spending += expense["amount"]
        
        
    if expense["amount"] > largest_expense['amount']:
        largest_expense = expense
        
    if expense['amount'] > 20000:
        expenses_above_20000.append(expense)
        
        
average_expense = total_spending/number_of_expenses
print(f"Total spending: {total_spending}")        
print(f"Food spending: {food_spending}")
print(f"Transport spending: {transport_spending}")
print(f"Number of Expenses: {number_of_expenses}")
print(f"Largest Expense: {largest_expense['amount']}")
print(f"Average Expense: {average_expense}")

for expense in expenses_above_20000:
    print(f"{expense['description']} - ₦{expense['amount']:,}")
        
        

