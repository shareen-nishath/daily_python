word = input("Enter any word: ")
vowels = "aeiouAEIOU"
v=0
c=0
for character in word:
    if ('a' <= character <= 'z') or ('A' <= character <= 'Z'):
        if character in vowels:
            v=v+1
        else:
            c=c+1

print("Vowels:",v)
print("Consonants:",c)
