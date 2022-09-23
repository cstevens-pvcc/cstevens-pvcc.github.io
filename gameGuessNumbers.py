# Name:
# NAME: 
# Program Purpose: Numbers guessing game

import random

line = '----------------------------------------------'
print(line)
print('GUESS-IN-6-GAME!')
print(line)
print('What is your name?')
name = input()

print(name + ', I am thinking of a number between 1 and 100.')
print('Can you guess it in 6 guesses or less?')
print(line)

number = random.randint(1,100)
guessesTaken = 0

for guessesTaken in range(6):
    print('Take a guess what the number is:')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('That is it, ' + name + '!')
    print('You guessed the number in '+ guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Sorry! The number I was thinking of was ' + number)

print(line)
