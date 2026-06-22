'''
Steps to game:

1. Pick a random word.
2. Get user input.
3. Make sure it is right.
4. Either make man get more parts or add letter to the letter bank of correct letters.
5. Tell user if they win of if they lose.
6. RESTART PROGRAM.
'''
import random

def get_letter():
    valid_input = False
    while not valid_input:
        try:
            letter_input = input("Guess a letter.").lower()[0]
            if letter_input>="a" or letter_input<="z":
                valid_input=True
                
        except ValueError:
            print("That is not a letter.")

    return letter_input

def in_the_word(user_input,game_word,guessed_letters):
    correct=False
    if user_input in game_word:
        correct=True
        
    else:
        correct=False
    guessed_letters.append(user_input)
    return correct



def main():
    words = ["Car", "Automobile", "Aerospace", "Monitor", "Mother", "Father", "Capsize" ]
    word_chooser = random.choice(words).lower()
    
    guessed_letters=[]
    display_word="-"*len(word_chooser)

    user_input=get_letter()



main()
