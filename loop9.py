grade=int(input("enter grade"))
count = 0
sum=0

while 0<=grade<=100 :
    if 60<=grade<=100 :
        sum+=grade
        count+=1
    grade = int(input("enter grade"))

print(int(sum/count))
