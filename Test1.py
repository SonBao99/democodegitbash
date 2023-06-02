#User enter a number (1, 100)
#Loop:
#- Computer think of a number

#if count > 7 -> lose

import random as rd

number = int(input('Enter a number (1- 100): '))
guess = 0
count = 0
low = 1 
high = 100
while number != guess:
    guess = (low + high) // 2
    print("computer guesses:", guess)
    count += 1
    if number < guess:
        print('Too low!')
        low = guess + 1
    elif number > guess:
        print('Too high!')
        high = guess - 1
    else:
        print('The computer has guessed the number!')
        break
    if count > 7:
        print('The computer took too many tries!')
        break
