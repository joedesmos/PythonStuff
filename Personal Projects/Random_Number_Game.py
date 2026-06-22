import random

# Generate random number between 1 and 100
random_number = random.randint(1, 100)

#Attempts counter
attempts = 0

#Game loop
guess = int(input("Guess a Number: "))
while guess != random_number:
    if guess < random_number:
        print("Too low!")
    else:
        print("Too high!")
    guess = int(input("Guess a Number: "))
print("Congrats! You guessed the number!")