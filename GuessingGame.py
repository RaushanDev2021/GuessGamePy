import random
computerGuess = random.randint(1, 10)
guess = 0
while guess != computerGuess:
    guess = input("Please enter your guess: ")
    guess = int(guess)
    if guess == computerGuess:
        print("Congratulations! You guessed it!")
    elif guess < computerGuess:
        print("Sorry, that's too low!")
    elif guess > computerGuess:
        print("Sorry, that's too high!")