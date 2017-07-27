a = [1, 1, 2, 3, 5, 8, 13, 21, 4, 4, 34, 55, 89]
b = [1, 2, 3, 1, 4, 4, 4, 5, 6, 7, 1, 8, 9, 1, 10, 11, 12, 13]
c = []
d = []

for i in b:
    if i in a:
        c.append(i)
c.sort()
print(c)
#the following code remove all the duplicates in c
test = (len(c))
for x in range(test):
    d.append(c[0])
    test1 = c[0]
    c.remove(c[0])
    if test1 in c:
        print('Duplicate - ' + str(c[0]))
        d.remove(c[0])

print(d)
