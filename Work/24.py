"""
How to play:

- Get 4 numbers
- Use basic operations to get to 24

"""

#imports
import random
import time

#Intro
def intro():
    print("Welcome to 24 - the game")
    time.sleep(1)
    print("\nHere are the rules of 24:\n- Get 4 numbers\n- Use basic operations to get to 24")
    print("\nLets start!")

#Game loop
def game():

    #Chooses a random four numbers
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    num3 = random.randint(1, 9)
    num4 = random.randint(1, 9)
    random_numbers = [num1, num2, num3, num4]
    print(num1)
    print(num2)
    print(num3)
    print(num4)

    #User picks numbers and operators
    choice1 = int(input("What is the first number in your equation?: "))
    choice2 = input("What is the first operator in your equation?: ")
    choice3 = int(input("What is the second number in your equation?: "))
    choice4 = input("What is the second operator in your equation?: ")
    choice5 = int(input("What is the third number in your equation?: "))
    choice6 = input("What is the third operator in your equation?: ")
    choice7 = int(input("What is the fourth number in your equation?: "))

    #Check for correct numbers
    if choice1 in random_numbers:
        pass
    else:
        print("No cheating!")
    if choice3 in random_numbers:
        pass
    else:
        print("No cheating!")
    if choice5 in random_numbers:
        pass
    else:
        print("No cheating!")
    if choice7 in random_numbers:
        pass
    else:
        print("No cheating!")
    
    #Converts second choice into operator
    if choice2 == "+":
        final_num1 = choice1 + choice3
    elif choice2 == "-":
        final_num1 = choice1 - choice3
    elif choice2 == "*":
        final_num1 = choice1 * choice3
    elif choice2 == "/":
        final_num1 = choice1 / choice3

    #Converts fourth choice into operator
    if choice4 == "+":
        final_num2 = final_num1 + choice5
    elif choice4 == "-":
        final_num2 = final_num1 - choice5
    elif choice4 == "*":
        final_num2 = final_num1 * choice5
    elif choice4 == "/":
        final_num2 = final_num1 / choice5

    #Converts sixth choice into operator
    if choice6 == "+":
        final_ans = final_num2 + choice7
    elif choice6 == "-":
        final_ans = final_num2 - choice7
    elif choice6 == "*":
        final_ans = final_num2 * choice7
    elif choice6 == "/":
        final_ans = final_num2 / choice7

    #Print final answer and check to see if the user won
    print(f"Your final answer was {final_ans}")
    if final_ans == 24:
        playagain = input("You won! Type 'y' to play again and 'n' to stop playing.")
        if playagain == "y":
            main()
        else:
            pass
    else:
        input("You lost :( Type 'y' to play again and 'n' to stop playing.")

def main():
    intro()
    game()

main()
