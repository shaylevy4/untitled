num=int(input("enter num"))
count=0
while num!=0 :
    num = int(input("enter num"))
    if num%7==0 or num%3==0:
        count+=1
print(count)