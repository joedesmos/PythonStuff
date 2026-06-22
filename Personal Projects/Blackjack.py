#Blackjack
#Made by Ryland DeSantis

#imports
import random
import time

#lists
Hit = ["Hit", "hit", "HIT", "h", "H"]
Stand = ["Stand", "stand", "STAND", "s", "S"]
Aces = [{"Ace of Clubs": 11}, {"Ace of Diamonds": 11}, {"Ace of Hearts": 11}, {"Ace of Spades": 11}]
Bet = ["Bet", "bet", "BET", "b", "B"]
Quit = ["Quit", "quit", "QUIT", "q", "Q"]

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

#variables
playing = True
choosing = False

#makes are variables equal to 0 and None
def variableReset():
    choseBet = False
    betOrQuit = True
    hitStand = True
    hitStand2 = True
    totalTimesDelt = 0
    chips = 25
    chipsBet = 0
    gameplayChoice = None
    hitOrStand = None
    dealerCard1 = None
    dealerCard2 = None
    dealerCard3 = None
    dealerCard4 = None
    dealerCardValue = 0
    dealerCardValue1 = 0
    dealerCardValue2 = 0
    dealerCardValue3 = 0
    dealerCardValue4 = 0
    dealerHand = None
    playerAce1 = None
    playerAce2 = None
    playerAce3 = None
    playerAce4 = None
    playerCard1 = None
    playerCard2 = None
    playerCard3 = None
    playerCard4 = None
    playerTotalCardValue = 0
    playerCardValue1 = 0
    playerCardValue2 = 0
    playerCardValue3 = 0
    playerCardValue4 = 0
    playerHand = None

#runs the variableReset function
variableReset()

#game
print("\nWelcome to blackjack!\n")
time.sleep(0.75)
print("Here are the rules of blackjack:\n\nYou will get assigned 2 cards and the dealer will get assigned 2 cards but you can only see 1 of the dealers cards. Your goal is to get closer to 21 than the dealer without going over.\nBlackjack pays 3/2.\n\nCard Values:\n\nNumber Cards = Their Number\nFace Cards = 10\nAces = 11 or 1")
time.sleep(5)
chips = 25
totalTimesDelt = 0

#game loop
while playing:

#resets variables to 0 and None to make sure nothing goes wrong later in the code
    variableReset()

#makes choosing run after random cards are selected and makes the choice for betting or quiting run
    choosing = True
    betOrQuit = True
    
#bet or quit logic

    if chips <= 0:
        print("\nYou went bankrupt!")
        playing = False
        print(f"Thanks for playing blackjack!\n\nStats:\nChips: {chips} chips\nTotal Chip Gain/Loss: {chips - 25} chips\nTotal Times Delt: {totalTimesDelt}\n")
        continue

    print(f"\nYou currently have {chips} chips.")

    while betOrQuit:
        try:
            gameplayChoice = input("\nWould you like to bet or quit?: ")
            if gameplayChoice in Bet or gameplayChoice in Quit:
                betOrQuit = False
                continue
            else:
                print("\nPlease chose one of the options!")
                continue
        except ValueError:
            print("\nPlease chose one of the options!")
            continue

#quit stats and logic
    if gameplayChoice in Quit:
        choseBet = False
        totalTimesDelt = totalTimesDelt
        playing = False
        print(f"\nThanks for playing blackjack!\n\nStats:\nChips: {chips} chips\nTotal Chip Gain/Loss: {chips - 25} chips\nTotal Times Delt: {totalTimesDelt}\n")
        continue

#betting logic
    if gameplayChoice in Bet:
        choseBet = True

    while choseBet:
        try:
            chipsBet = int(input("\nHow many chips would you like to bet?: "))

            if chipsBet > chips:
                print("\nYou can't go in debt!")
                time.sleep(0.25)
                continue
            elif chipsBet <= chips:
                choseBet = False
                continue
        except ValueError:
            print("\nPlease type in a number!")
            time.sleep(0.25)
            continue

#random choice of cards
    drawnCards = random.sample(cards, 8)

    playerCard1 = drawnCards[0]
    playerCard2 = drawnCards[1]
    playerCard3 = drawnCards[2]
    playerCard4 = drawnCards[3]
    dealerCard1 = drawnCards[4]
    dealerCard2 = drawnCards[5]
    dealerCard3 = drawnCards[6]
    dealerCard4 = drawnCards[7]

#giving cards value 
    playerCardValue1 = list(playerCard1.values())[0]
    playerCardValue2 = list(playerCard2.values())[0]
    playerCardValue3 = list(playerCard3.values())[0]
    playerCardValue4 = list(playerCard4.values())[0]
    dealerCardValue1 = list(dealerCard1.values())[0]
    dealerCardValue2 = list(dealerCard2.values())[0]
    dealerCardValue3 = list(dealerCard3.values())[0]
    dealerCardValue4 = list(dealerCard4.values())[0]

#deleting selected cards from the deck after being chosen
    for card in drawnCards:
        cards.remove(card)

#adding cards back after being deleted
    for card in drawnCards:
        cards.append(card)

#functions
    def playerStand():
        global chips, chipsBet

        print(f"\nThe dealer had a {dealerCard1} and a {dealerCard2}.")

        dealerTotalCardValue = dealerCardValue1 + dealerCardValue2

        if dealerTotalCardValue < 17:
            print("\nThe dealer hit.")
            dealerTotalCardValue += dealerCardValue3
            time.sleep(1)
            
            if dealerTotalCardValue < 17:
                print("\nThe dealer hit again.")
                dealerTotalCardValue += dealerCardValue4
                time.sleep(1)

                if dealerTotalCardValue > 21:
                    if list(dealerCard1.keys())[0].startswith("Ace") and list(dealerCard1.values())[0] == 11:
                        cardKey = list(dealerCard1.keys())[0]
                        dealerCard1[cardKey] = 1
                    elif list(dealerCard2.keys())[0].startswith("Ace") and list(dealerCard2.values())[0] == 11:
                        cardKey = list(dealerCard2.keys())[0]
                        dealerCard2[cardKey] = 1
                    elif list(dealerCard3.keys())[0].startswith("Ace") and list(dealerCard3.values())[0] == 11:
                        cardKey = list(dealerCard3.keys())[0]
                        dealerCard3[cardKey] = 1
                    else:
                        time.sleep(1)
                        print(f"\nYou won {chipsBet*2} chips! The dealer bust!")
                        chips = (chipsBet*2 + chips)
                        hitStand = False
                        time.sleep(1)

        print(f"\nThe dealer has a value of {dealerTotalCardValue} and you have a value of {playerTotalCardValue}.")

        if dealerTotalCardValue > 21:
            if list(dealerCard1.keys())[0].startswith("Ace") and list(dealerCard1.values())[0] == 11:
                cardKey = list(dealerCard1.keys())[0]
                dealerCard1[cardKey] = 1
            elif list(dealerCard2.keys())[0].startswith("Ace") and list(dealerCard2.values())[0] == 11:
                cardKey = list(dealerCard2.keys())[0]
                dealerCard2[cardKey] = 1
            elif list(dealerCard3.keys())[0].startswith("Ace") and list(dealerCard3.values())[0] == 11:
                cardKey = list(dealerCard3.keys())[0]
                dealerCard3[cardKey] = 1
            elif list(dealerCard4.keys())[0].startswith("Ace") and list(dealerCard4.values())[0] == 11:
                cardKey = list(dealerCard4.keys())[0]
                dealerCard4[cardKey] = 1
            else:
                time.sleep(1)
                print(f"\nYou won {chipsBet*2} chips! The dealer bust!")
                chips = (chipsBet*2 + chips)
                hitStand = False
                time.sleep(1)

        elif dealerTotalCardValue > playerTotalCardValue:
            print(f"\nSorry, you lost {chipsBet} chips.")
            chips = (chips - chipsBet)
        elif dealerTotalCardValue < playerTotalCardValue:
            print(f"\nYou won {chipsBet*2} chips!")
            chips = (chipsBet*2 + chips)
        else:
            print(f"\nIts a push! No chips lost or won.")

    while choosing:

        #Only runs once so that cards can be reselected
        choosing = False

    #cards drawn
        dealerTotalCardValue = dealerCardValue1 + dealerCardValue2
        playerTotalCardValue = playerCardValue1 + playerCardValue2
        
        totalTimesDelt += 1
        time.sleep(0.5)
        print(f"\nThe dealer has a {dealerCard1}.")
        print(f"\nYou have a {playerCard1} and a {playerCard2}. Value = {playerTotalCardValue}")

    #blackjack logic
        if dealerTotalCardValue == 21:
            print(f"\nDealer has a {dealerCard1} and a {dealerCard2}, so they got blackjack! You lost {chipsBet} chips.\n")
            chips = (chips - chipsBet)
            continue

        elif playerTotalCardValue == 21:
            print(f"\nYou got blackjack and won {chipsBet*2.5} chips!\n")
            chips = (chipsBet*2.5 + chips)
            continue

        else:

            gameChoice = input("\nWould you like to hit or stand?: ")
            hitStand = True

        # hitting and standing logic / loop
            while hitStand:
                try:
                    if gameChoice in Hit:
                        #hit logic
                        playerTotalCardValue = playerCardValue1 + playerCardValue2 + playerCardValue3
                        print(f"\nYou now have a {playerCard1}, a {playerCard2}, and a {playerCard3}. Value = {playerTotalCardValue}\n")
                        
                        #Ace logic
                        if playerTotalCardValue > 21:

                            if list(playerCard1.keys())[0].startswith("Ace") and list(playerCard1.values())[0] == 11:
                                cardKey = list(playerCard1.keys())[0]
                                playerCard1[cardKey] = 1
                            elif list(playerCard2.keys())[0].startswith("Ace") and list(playerCard2.values())[0] == 11:
                                cardKey = list(playerCard2.keys())[0]
                                playerCard2[cardKey] = 1
                            elif list(playerCard3.keys())[0].startswith("Ace") and list(playerCard3.values())[0] == 11:
                                cardKey = list(playerCard3.keys())[0]
                                playerCard3[cardKey] = 1
                            else:
                                time.sleep(1)
                                print(f"You bust and lost {chipsBet} chips!\n")
                                chips = (chips - chipsBet)
                                hitStand = False
                                time.sleep(1)
                                continue

                        else:
                            #continue to hit logic
                            hitOrStand = input("Would you like to hit or stand?: ")
                            if hitOrStand in Hit:
                                playerTotalCardValue = playerCardValue1 + playerCardValue2 + playerCardValue3 + playerCardValue4
                                print(f"\nYou now have a {playerCard1}, a {playerCard2}, a {playerCard3}, and a {playerCard4}. Value = {playerTotalCardValue}\n")

                                #Ace logic
                                if playerTotalCardValue > 21:

                                    if list(playerCard1.keys())[0].startswith("Ace") and list(playerCard1.values())[0] == 11:
                                        cardKey = list(playerCard1.keys())[0]
                                        playerCard1[cardKey] = 1
                                    elif list(playerCard2.keys())[0].startswith("Ace") and list(playerCard2.values())[0] == 11:
                                        cardKey = list(playerCard2.keys())[0]
                                        playerCard2[cardKey] = 1
                                    elif list(playerCard3.keys())[0].startswith("Ace") and list(playerCard3.values())[0] == 11:
                                        cardKey = list(playerCard3.keys())[0]
                                        playerCard3[cardKey] = 1
                                    elif list(playerCard4.keys())[0].startswith("Ace") and list(playerCard4.values())[0] == 11:
                                        cardKey = list(playerCard4.keys())[0]
                                        playerCard4[cardKey] = 1
                                    else:
                                        time.sleep(1)
                                        print(f"You bust and lost {chipsBet} chips!\n")
                                        chips = (chips - chipsBet)
                                        hitStand = False
                                        time.sleep(1)
                                        continue
                                
                                playerCardValue1 = list(playerCard1.values())[0]        
                                playerCardValue2 = list(playerCard2.values())[0]
                                playerCardValue3 = list(playerCard3.values())[0]  
                                playerCardValue4 = list(playerCard4.values())[0]  

                            elif hitOrStand in Stand:
                                playerStand()
                                hitStand = False
                                continue

                    elif gameChoice in Stand:
                        playerStand()
                        hitStand = False
                        continue

                    else:
                        #mistype in hit or stand
                        print("Please chose one of the options!")
                        gameChoice = input("\nWould you like to hit or stand?: ")
                        continue

                except ValueError:
                    #value error in hit or stand
                    print("Please chose one of the options!")
                    continue
