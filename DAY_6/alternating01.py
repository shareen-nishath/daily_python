n = 5
for i in range(1, n+1):
    length = i 
    if i % 2 == 1:
        start = 0
    else:
        start = 1
    for j in range(length):
        print(start, end="")
        if start == 0:
            start = 1
        else:
            start = 0
    print()  
