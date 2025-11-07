word=str(input("Enter a word:"))
vowels=["a","e","i","o","u"]
count = 0
for i in word:
    if i in vowels:
        count +=1
if count>0:
    print(count)
else:
    print("No vowels")