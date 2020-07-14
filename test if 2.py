num1=int(input("enter num "))
num2=num1%10
num3=num1//10%10
num4=num1//100
if 100<=num1<1000 :
    print(num2+num3+num4)
else:
    print("false")
