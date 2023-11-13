import random
from art import logo

print(logo)

print('''Welcome to the Number Guessing Game!\n
I\'m thinking of a number between 1 and 100.\n''')
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

EASY = 10
HARD = 5

secret_number = random.randint(1,100)
print(secret_number)

if difficulty == "easy":
    attempts = EASY
else:
    attempts = HARD
 
def guess(attempts): 
    print(f"You have {attempts} attempts remaining to guess the number")
    guess_number  = int(input("Make a guess: "))
    #print(guess)
    if guess_number < 1 or guess_number > 100:
        print("Invalid number")
    return guess_number
 
correct = False 
while attempts > 0 and correct == False:
    guessed = guess(attempts)
    if guessed == secret_number:
        print(f"You got it!, The answer was {secret_number}")
        correct = True
    elif guessed > secret_number:
        print("Too high.")
        if attempts > 1:
            print("Guess again.")
    elif guessed < secret_number:
        print("Too low.")
        if attempts > 1:
            print("Guess again.")
    attempts -= 1

if attempts == 0 and correct == False:
    print("You've run out of guesses, you lose.")
