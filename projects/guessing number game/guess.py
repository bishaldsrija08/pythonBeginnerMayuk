# Making number guessing game
import random

def guess(x):
    random_number = random.randint(1,x)
    count =0
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number bewtween 1 and {x}: '))
        count = count + 1
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
    print(f'Yay, congrats. You have guessed the number {random_number} correctly! You made {count} guesses.')


x = int(input('Enter the upper limit for the number guessing game: '))
guess(x)