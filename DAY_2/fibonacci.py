n = int(input("Enter numbers: "))
a = 0
b = 1
if n == 1:
    print(a)
else:
    print(a, b, end=" ")
    for i in range(2, n):
        c = a + b
        print(c, end=" ")
        a = b
        b = c





# 0, 1 is starting
# when add the previous both digits you getthe next digits
# start for loop rnage from 2 as 0 and 1 are first two digits
# c is adding previous numbers
# and printing it with space
# so now the new one becomes b and previous is a