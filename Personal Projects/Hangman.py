#Hangman
#Made by Ryland DeSantis

#imports
import random
import time

#variables
quesses = 0
avaliableGuesses = 6
word = None
computerWord = None


#lists
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',' u', 'v', 'w', 'x', 'y', 'z']
words = ['apple', 'banana', 'car']

#functions
def computerPickWord():
    computerWord = random.choice(words)
    print(computerWord)
    words = words.append[computerWord:]
    print(words)


#game
computerPickWord()