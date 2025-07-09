# welcome message
print('welcome to my island')
door = input('There are tow doors in front of you. a red door and a blue door\nWhich door do you want to open?').lower()
if door == 'red':
    print('Great! now you entered a room.')
    box = input('You found three boxes:white,black,green\nWhich box do you open!').lower()
    if box == 'white':
        print('Opes! You opened a box filled with snakes')
    elif box == 'black':
        print('Opes! You opened a box filled with spiders')
    elif box == 'green':
        print('Congratulations! You found the treasure!')
    else:
        print('invalid choice!')
elif door == 'blue':
    print('Opes! You chose the crocodile door\nGame Over.')
else:
    print('invalid choice!')