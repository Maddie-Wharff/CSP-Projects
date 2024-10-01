age = int(input("How old are you?: "))
if age >= 18:
    print("You are old enough to vote!")
elif age >= 16:
    print("You are old enough to drive!")
elif age >= 15:
    print("You are old enough to get a learner's permit!")
elif age >= 5:
    print("You are old enough to go to school!")
else:
    print("You are too young to go to school. :(")