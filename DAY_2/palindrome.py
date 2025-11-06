word = str(input("type any word to check palindrome"))
if word == word[::-1]:
    print("palindrome")
else: 
    print("Not palindroem")