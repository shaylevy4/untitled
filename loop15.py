grade = int(input("enter grade: "))
count = 0
sum1 = 0
max1 = 0
while 0 <= grade <= 100:
    count += 1
    sum1 += grade
    if max1 < grade and 0 <= grade <= 100:
        max1 = grade

    grade = int(input("enter num"))

print(max1, int(sum1 / count), max1 - int(sum1 / count))
