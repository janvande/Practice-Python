a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
listLength = len(a)
for i in range(listLength):
    if a[i] < 5:
        b.append(a[i])
        print(str(a[i]) + ' is less then 5')
    else:
        print(str(a[i]) + ' is equal or greater than 5')
print('From ' + str(a) + ', The following numbers are less than 5;')
print (str(b))




