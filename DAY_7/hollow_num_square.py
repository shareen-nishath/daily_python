n = 4
for i in range(1, n + 1):
    if i == 1 or i == n:
        print("1" * n)
    else:
        print("1" + " " * (n - 2) + "1")
