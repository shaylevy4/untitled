day=int(input("enter day "))
month=int(input("enter month "))
year=int(input("enter year "))

if 1<=day<=31 and 1<=month<=12 and 1950<=year<=2020:
    print(day,"/",month,"/",int(year%100//10),(year%10),sep=(""))
else:
    print("invallid")
