import pydealer as pd
from player import Player
from const import *

def nextHand(hands, deck):
    for hand in hands:
        hand.clear()
        hand.add_card(2, deck)


def startGame(hands, numberOfPlayers, deck):
    for i in range(numberOfPlayers + 1):
        hands.append(Player(pd.Stack()))
        hands[i].add_card(2, deck)


def runGame():
    shoe = pd.Deck(rebuild=True, shuffle=True, ranks=BLACKJACK_RANKS)
    shoe.shuffle()
    hands = list() 

    winloss = 0
    startGame(hands, 1, shoe)

    for i in range(40):
        hands[1].playerStrategy(hands[0].hand[0], shoe)
        if hands[1].getValue() != -1:
            hands[0].dealerStrategy(shoe)
            if hands[0].getValue() > hands[1].getValue():
                winloss -= 1
            else:
                winloss += 1
        else:
            winloss -= 1
        nextHand(hands, shoe)
    print(winloss)

if __name__ == "__main__":
    runGame()







