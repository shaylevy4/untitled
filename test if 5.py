num1=int(input("enter num "))
num2=int(input("enter num "))

if num1%2==0 and num2%2==0 :
    print(num1+num2)
else:
    if num1%2!=0 and num2%2!=0 :
        print(num1*num2)
    else:
        if num1%2==0 and num2%2!=0 :
            print(num1*num2)
        else:
            if num1%2!=0 and num2%2==0 :
                print(num1*num2)