print("This is going to calculate your budget for this month.")
income = float(input("How much do you make every month?: "))
print(f"Your income is: ${income:.2f}")
rent = float(input("How much is rent?: "))
utilities = float(input("How much are utilities?: "))
groceries = float(input("How much are groceries?: "))
transportation = float(input("How much is transportation?: "))
expenses = rent + utilities + groceries + transportation
savings = income * 0.2
total = income - expenses - savings
prent = rent / income
putilities = utilities / income
pgroceries = groceries / income
ptransportation = transportation / income
pexpenses = expenses / income
print(f"Your expenses are: ${expenses:.2f}")
print(f"Your savings are: ${savings:.2f}")
print(f"Your total left to spend is: ${total:.2f}")
print(f"Your rent is {prent:.2%} of your income")
print(f"Your utilities are {putilities:.2%} of your income")
print(f"Your groceries are {pgroceries:.2%} of your income")
print(f"Your transportation is {ptransportation:.2%} of your income")
print(f"Your expenses are {pexpenses:.2%} of your income")