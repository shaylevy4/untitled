sum1=0
ave=0
count=0

for i in range(6) :
    num=int(input("enter num"))
    if num%2==0:
        count+=1
        sum1+=num

print(int(sum1/count))
print(sum1)

