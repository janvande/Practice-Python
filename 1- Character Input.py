print('This Program will ask your Name and Age, it will than calculate what year you will be 100')
yourName = input('What is your name?  ')
yourAge = input('What is your age?  ')
print('Your name is ' + yourName + ' and you are ' + yourAge + ' years old.')
age100 = (100 - 46) + 2017
print('You will be 100 in the year ' + str(age100))
repeat = input('How many times would you like to repeat the previous message?  ')
print('We will repeat the message ' + repeat + ' Times.')
print()
for i in range(int(repeat)):
    print('You will be 100 in the year ' + str(age100))
