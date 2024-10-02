import datetime
now = datetime.datetime.now().hour
print(now)


if now <= 12:
    print("Good morning!")
elif now <= 18:
    print("Good afternoon!")
elif now <= 20:
    print("Good evening!")
else:
    print("Good night!")