number = int(input("Enter a number to see its multiplication table:"))

for x in  range(1, 10+1):
    print (f"{number}  * {x} = ",number*x, end="" )
    print()
