inputNumber = int(input('Please input any number, I will tell you if it is odd or even. '))
oddEven = inputNumber/2 - inputNumber//2

if oddEven == 0:
    print('Even')
else:
    print('Odd')
print('Thank you!')

devide4 = inputNumber/4 - inputNumber//4

if devide4 == 0:
    print(str(inputNumber) + ' Is a multiple of 4')
else:
    print(str(inputNumber) + ' Is NOT a multiple of 4')

