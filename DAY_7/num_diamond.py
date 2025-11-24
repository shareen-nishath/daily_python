n = 4
for i in range(1, n + 1):
    line = ""
    for j in range(1, i + 1):
        line += str(j)
    for j in range(i - 1, 0, -1):
        line += str(j)
    print(line)

for i in range(n - 1, 0, -1):
    line = ""
    for j in range(1, i + 1):
        line += str(j)
    for j in range(i - 1, 0, -1):
        line += str(j)
    print(line)
