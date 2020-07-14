grade=int(input("enter num"))
sum=0
sum1=0
count=0
count1=0

while 0<=grade<=100 :
    if 60 <= grade :
        sum += grade
        count += 1
    else:
        sum1 += grade
        count1 += 1
    grade = int(input("enter num"))
print(sum/count,sum1/count1)

