import time
import random

userCard1 = None
userCard2 = None
flopCard1 = None
flopCard2 = None
flopCard3 = None

#cards with their values
cards = [
    {"2 of Spades": 2}, {"3 of Spades": 3}, {"4 of Spades": 4}, {"5 of Spades": 5}, {"6 of Spades": 6}, {"7 of Spades": 7},
    {"8 of Spades": 8}, {"9 of Spades": 9}, {"10 of Spades": 10}, {"Jack of Spades": 10}, {"Queen of Spades": 10},
    {"King of Spades": 10}, {"Ace of Spades": 11},

    {"2 of Hearts": 2}, {"3 of Hearts": 3}, {"4 of Hearts": 4}, {"5 of Hearts": 5}, {"6 of Hearts": 6}, {"7 of Hearts": 7},
    {"8 of Hearts": 8}, {"9 of Hearts": 9}, {"10 of Hearts": 10}, {"Jack of Hearts": 10}, {"Queen of Hearts": 10},
    {"King of Hearts": 10}, {"Ace of Hearts": 11},

    {"2 of Diamonds": 2}, {"3 of Diamonds": 3}, {"4 of Diamonds": 4}, {"5 of Diamonds": 5}, {"6 of Diamonds": 6},
    {"7 of Diamonds": 7}, {"8 of Diamonds": 8}, {"9 of Diamonds": 9}, {"10 of Diamonds": 10}, {"Jack of Diamonds": 10},
    {"Queen of Diamonds": 10}, {"King of Diamonds": 10}, {"Ace of Diamonds": 11},

    {"2 of Clubs": 2}, {"3 of Clubs": 3}, {"4 of Clubs": 4}, {"5 of Clubs": 5}, {"6 of Clubs": 6}, {"7 of Clubs": 7},
    {"8 of Clubs": 8}, {"9 of Clubs": 9}, {"10 of Clubs": 10}, {"Jack of Clubs": 10}, {"Queen of Clubs": 10},
    {"King of Clubs": 10}, {"Ace of Clubs": 11}
]

def deal():
    userCard1 = random.choice(list(cards))
    print(userCard1)
    userCard2 = random.choice(list(cards))
    if userCard2 == userCard1:
        userCard2 = random.choice(list(cards))
    print(userCard2)

def flop():
    flopCard1 = random.choice(list(cards))
    if flopCard1 == userCard1 or flopCard1 == userCard2:
        flopCard1 = random.choice(list(cards))
    print(flopCard1)
    flopCard2 = random.choice(list(cards))
    if flopCard2 == userCard1 or flopCard2 == userCard2 or flopCard2 == flopCard1:
        flopCard2 = random.choice(list(cards))
    print(flopCard2)
    flopCard3 = random.choice(list(cards))
    if flopCard3 == userCard1 or flopCard3 == userCard2 or flopCard3 == flopCard1 or flopCard3 == flopCard2:
        flopCard3 = random.choice(list(cards))
    print(flopCard3)

def main():
    print("Welcome to Poker!")
    time.sleep(0.5)
    print("\nhRules of Poker:\n\nThree cards will be handed out that is called the flop. Next, a fourth card will be handed out that is called the turn. Lastly, when the fifth and final card is handed out that is called the river.\nYour goal is to make the best hand of five cards as possible with your two cards you got dealt and the 5 cards that got dealt.\n\nPoker Hand List(In Order of Best to Worst):\nRoyal Flush: Ace, King, Queen, Jack, 10 of the same suit\nStraight Flush: Five consecutive cards of the same suit\nFour of a Kind: Four cards of the exact same rank\nFull House: Three of a kind plus a pair\nFlush: Five cards of the same suit, not in order\nStraight: Five consecutive cards of mixed suits\nThree of a Kind: Three cards of the same rank\nTwo Pair: Two different pairs in one hand\nOne Pair: Two cards of the same rank\nHigh Card: The highest card when no combination is made.")
    time.sleep(5)
    print("Here are your cards:\n")
    deal()
    time.sleep(0.5)
    print("Flop:")
    flop()

main()