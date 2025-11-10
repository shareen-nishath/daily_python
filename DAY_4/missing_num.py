a = list(map(int, input("Enter numbers sepr by space: ").split()))
for i in range(len(a)-1):
    if a[i+1] != a[i] + 1:
        print("Missing number is:", a[i] + 1)
        break
