n = 5
num = 1
for i in range(1, n + 1):
    line = ""
    for j in range(i):
        line += str(num) + " "
        num += 1
    print(line)
