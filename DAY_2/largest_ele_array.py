a = [int(x) for x in input("Enter the list of array: ").split()]
result = a[0]
for i in a:
    if i> result:
        result = i
print(result)






# a = [1,3,2,4]
# result = 1
# loop in array
# so if the current element is greater than 1 which is result thats the answer.