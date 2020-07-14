str1=str(input("enter words "))
print(len(str1))
print(str1[2:6])
list=str1.split(" ")
print(list[0]*3)
for word in list:
    print(word.capitalize(),end=" ")