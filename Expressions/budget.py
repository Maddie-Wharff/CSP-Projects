print("This will calculate your budget for the month.")
income = input("How much do you make in a month?: ")
rent = input("How much is rent?: ")
utilities = input("How much are utilities?: ")
groceries = input("How much are groceries?: ")
transportation = input("How much is transportation?: ")
expenses = rent+utilities+groceries+transportation
savings = income*.2
total = income-expenses-savings
prent = rent/income*100
putilities = utilities/income*100
pgroceries = groceries/income*100
ptransportation = transportation/income*100
pexpenses = expenses/income*100
print("Your total expenses are:" expenses)