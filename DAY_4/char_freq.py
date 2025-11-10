characters=input("Enter a word: ")

for i in characters:
    count=0
    for j in characters:
        if i == j:
            count +=1
    print(i,"=",count)
