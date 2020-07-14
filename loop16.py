password = input("enter password")
password1 = input("enter password")
count = 0
while password1 != password:
    count += 1
    if count == 5:
        print("failed")
        break
    password1 = input("enter agian")
else:
    print("good")
