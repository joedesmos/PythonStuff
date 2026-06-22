import random


valid_choice = False
while not valid_choice:
    choice=input("Pick r, p, or s for rock paper scissors.")
    if choice == 'r' or choice == 'p' or choice == 's':
        valid_choice = True
    else:
        print("Pick the right thing.")

computer_choice = random.choice(['r', 'p', 's'])

print()
