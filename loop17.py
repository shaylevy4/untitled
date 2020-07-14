factor = int(input("enter factor"))
factor1 = factor / 100
sum2 = 0
count = 0
sum1 = 0
for i in range(5):
    grade = int(input("enter grade"))
    sum2 += (grade + (grade * factor1))
    sum1 += grade
    count += 1
    print(grade + (grade * factor1))

print(sum2 / count, sum1 / count)
print((sum2 / count) - (sum1 / count))
