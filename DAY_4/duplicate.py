a = list(map(int, input("Enter numbers: ").split()))
no_duplicate=[]
for i in a:
    if i not in no_duplicate:
        no_duplicate.append(i)
print(no_duplicate)
