# Computer Number Guesser
# Made by Ryland DeSantis

import random
import time

#List
numbersGuessed = []

#Variables
attempts = 0
computerGuess = 0
randomNumber = 0
guessing = True
program = True

#Program
while program:

    randomNumber = random.randint(1,100)
    print(f"The number chosen is: {randomNumber}")
    time.sleep(0.5)

    while guessing:
        computerGuess = random.randint(1,100)

        if computerGuess == randomNumber:
            print(computerGuess)
            print(f"The computer guessed the number in {attempts} attempts")
            print(f"It took the computer {timeTaken} seconds to guess the number.")
            print(numbersGuessed)
            guessing = False
            program = False
            continue
        elif computerGuess not in numbersGuessed:
            numbersGuessed.append(computerGuess)
            attempts += 1
            print(computerGuess)
            time.sleep(0.1)

        elif computerGuess in numbersGuessed:
            continue

