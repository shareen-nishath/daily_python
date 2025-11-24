n = 5
for i in range(1, n + 1):
    line = ""
    for j in range(i):
        line += chr(65 + j)
    for j in range(i - 2, -1, -1):
        line += chr(65 + j)
    print(line)
