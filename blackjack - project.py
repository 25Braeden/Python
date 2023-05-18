import os
import random
deck = (2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "K", "Q", "A") * 4
def firstHand(deck): #deal the first hand
    hand = []
    counter = 0
    while counter < 2: #deal two cards
        x = random.randint(0, 51)
        hand.append(deck[x])
        counter += 1
    return hand
def HandValue(hand):
    value = 0
    for card in hand:
        if card == "J":
            value += 10
        if card == "Q":
            value += 10
        if card == "K":
            value += 10
        if card == "A":
            if value <= 10: #add 11 if hand value is less than/equal to 10
                value += 11
            else:
                value += 1
        if card == 2: value += 2
        if card == 3: value += 3
        if card == 4: value += 4
        if card == 5: value += 5
        if card == 6: value += 6
        if card == 7: value += 7
        if card == 8: value += 8
        if card == 9: value += 9
        if card == 10: value += 10
    return value
def hit(hand):
 x = random.randint(0,51)
 hand.append(deck[x])
 return hand
def playAgain():
    yesNo = raw_input("Do you want to play again? (yes/no)").lower()
    if yesNo == "yes":
        dealersHand = []
        playersHand = []
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4
        play()
    else:
        print("See you")
        exit()
def clear(): #clear the system
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')
def printResults(playersHand, dealersHand):
    clear()
    print("The dealer holds a " + str(dealersHand) + " for a total of " + str(HandValue(dealersHand)))
    print("You hold a " + str(playersHand) + " for a total of " + str(HandValue(playersHand)))
def doYouWin(playersHand, dealersHand):
    if HandValue(playersHand) == 21:
        printResults(playersHand, dealersHand)
        print("You win with a blackjack!")
    elif HandValue(dealersHand) == 21:
        printResults(playersHand, dealersHand)
        print("You lose. The dealer got a blackjack.")
    elif HandValue(playersHand) > 21:
        printResults(playersHand, dealersHand)
        print("You busted. You lose.")
    elif HandValue(dealersHand) > 21:
        printResults(playersHand, dealersHand)
        print("The dealer busted. You win!")
    elif HandValue(playersHand) > HandValue(dealersHand):
        printResults(playersHand, dealersHand)
        print("Your score is higher than the dealer's. You win!")
    elif HandValue(playersHand) < HandValue(dealersHand):
        printResults(playersHand, dealersHand)
        print("Your score is lower than the dealer's. You lose.")


def blackjackPerhaps(playersHand, dealersHand):
 if HandValue(playersHand) == 21:
     print("You won with a blackjack")
     playAgain()
 elif dealersHand == 21:
     print("The dealer won with a blackjack.")
     playAgain()
def play():
    stayHitOrQuit = ""
    clear()
    print("Hi! Welcome to Blackjack!")
    playersHand = firstHand(deck) #deal the first hand
    dealersHand = firstHand(deck)
    while stayHitOrQuit != "quit":
         print("The dealer is showing a " + str(dealersHand[0]))
         print("You have are holding a " + str(playersHand[0]) + " and " + str(playersHand[1]) + ".")
         blackjackPerhaps(playersHand, dealersHand) #is anyone dealt a blackjack
         stayHitOrQuit = raw_input("Do you want to hit, stay, or quit?").lower()
         clear()
         if stayHitOrQuit == "hit":
             hit(playersHand)
             while HandValue(dealersHand) < 17:
                 hit(dealersHand)
             doYouWin(playersHand, dealersHand)
             playAgain()
         elif stayHitOrQuit == "stay":
             while HandValue(dealersHand) < 17:
                 hit(dealersHand)
             doYouWin(playersHand, dealersHand)
             playAgain()
play()
