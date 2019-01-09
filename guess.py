import random

guessesTaken = 0

print('Hello! What is yout name?')
myName = input()

number = random.randint(1, 20)
print(f'Well, {myName}, I am thinking of a number between 1 and 20')

while guessesTaken < 2:
    print('Take a guess.')
    guess = input()
    guess = int(guess)


    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Your guess is too low.')
    
    if guess > number:
        print('Your guess is too high')

    if guess == number:
        break

# with f string we don't need to convert the values
if guess == number:
    # guessesTaken == str(guessesTaken)
    print(f'Good job, {myName}! You guessed my number in {guessesTaken} guesses!')

if guess != number:
    # number = (str(number))
    print(f'Nope. The number I was thinking of was {number}')
