import random


valid_choice = False
while not valid_choice:
    choice=input("Pick r, p, or s for rock paper scissors.")
    if choice == 'r' or choice == 'p' or choice == 's':
        valid_choice = True
    else:
        print("Pick the right thing.")

computer_choice = random.choice(['r', 'p', 's'])

if choice == "r" and computer_choice == "p":
    print("You Lose!")
elif choice == "p" and computer_choice == "s":
    print("You Lose!")
elif choice == "s" and computer_choice == "r":
    print("You Lose!")
else:
    print("You Win!")
