def percent(type, amount):
    per = amount/income*100
    return f"Your {type} is {per}%  of your income." 

def usr(type):
    response = float(input(f"How much is your {type}?: \n"))
    return response

print("This is going to calculate your budget for this month.")
income = usr("income")
rent = usr("rent")
utilities = usr("utilities")
groceries = usr("groceries")
transportation = usr("transportation")

expenses = rent + utilities + groceries + transportation
savings = income*0.2
total = income - expenses - savings

print(f"Your expenses are: ${expenses:.2f}")
print(f"Your savings are: ${savings:.2f}")
print(f"Your total left to spend is: ${total:.2f}")

print(percent("rent", rent))
print(percent("utilities", utilities))
print(percent("groceries", groceries))
print(percent("transportation", transportation))
print(percent("expenses", expenses))