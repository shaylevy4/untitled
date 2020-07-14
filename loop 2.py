age=int(input("enter age "))

while age<0 or age>120:
    age = int(input("enter age "))
if 0 <= age <= 18:
        print("child")
elif 19 <= age <= 60:
        print("adult")
elif 61 <= age <= 120:
        print("senior")