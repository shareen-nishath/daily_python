n = 5
letters = "ABCDEFG"
for i in range(1, n+1):   
    for j in range(i):     
        print(letters[j], end="")
    print()
