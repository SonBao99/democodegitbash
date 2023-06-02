#User enter a number (1, 100)
#Loop:
#- Computer think of a number

#if count > 7 -> lose

import random as rd

number = int(input('Enter a number (1- 100): '))
guess = rd.randint(1,100)

while number != guess:
    if number < guess:
        print('Too low!')
    elif number > guess:
        print('Too high!')
    else:
        print('The computer has guessed the number!')
        
