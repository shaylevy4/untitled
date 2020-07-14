num=int(input("enter num"))
min=0
while num!=0 :
    if (min>num or min==0) and num>0:
        min=num
    num = int(input("enter num"))
print(min)
