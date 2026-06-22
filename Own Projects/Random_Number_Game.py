import random

random_number = random.randint(1, 100)
guesses = 0
guess = None

while guess != random_number:
    try:
        guess = int(input("Guess a number 1-100: "))
        guesses += 1

        if guess > random_number:
            print("Too High")

        elif guess < random_number:
            print("Too Low")

        else:
            print(f"You guessed the number in {guesses} attempts.")

    except ValueError:
        print("Please type a number")