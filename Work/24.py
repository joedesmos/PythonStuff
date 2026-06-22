"""
How to play:

- Get 4 numbers
- Use basic operations to get to 24

"""

#imports
import random
import time

#variables and lists
num1 = 0
num2 = 0
num3 = 0
num4 = 0
random_numbers = []

#Choose the four random numbers
def choose_numbers():
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    num3 = random.randint(1, 9)
    num4 = random.randint(1, 9)
    random_numbers = [num1, num2, num3, num4]

#Intro
def intro():
    print("Welcome to 24 - the game")
    time.sleep(1)
    print("\nHere are the rules of 24:\n- Get 4 numbers\n- Use basic operations to get to 24")
    print("\nLets start!")

#Game loop
def game():
    choose_numbers()

    print(num1)
    print(num2)
    print(num3)
    print(num4)

    choice1 = int(input("What is the first number in your equation?: "))
    choice2 = int(input("What is the first operator in your equation?: "))
    choice3 = int(input("What is the second number in your equation?: "))
    choice4 = int(input("What is the second operator in your equation?: "))
    choice5 = int(input("What is the third number in your equation?: "))
    choice6 = int(input("What is the third operator in your equation?: "))
    choice7 = int(input("What is the fourth number in your equation?: "))

    if choice1 in random_numbers:
        pass
    else:
        print("No cheating")
    if choice3 in random_numbers:
        pass
    else:
        print("No cheating")
    if choice5 in random_numbers:
        pass
    else:
        print("No cheating")
    if choice7 in random_numbers:
        pass
    else:
        print("No cheating")

    final_answer = ""

def main():
    intro()

main()
