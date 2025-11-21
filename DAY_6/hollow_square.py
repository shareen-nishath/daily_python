n = 5
for i in range(1, n+1):
    if i == 1 or i == 5:
        print("*" *5)
    else:
        print("*"+ " "*(n-2)+"*")