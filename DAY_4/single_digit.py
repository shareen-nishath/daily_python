n = int(input("Enter a number: "))

while n>9:  
    total=0
    while n>0:
        digit= n%10
        total= total+digit
        n= n//10
    n=total
print(n)
