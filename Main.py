import pydealer as pd
import random
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
    players = list() 

    winloss = 0
    startGame(players, 1, shoe)

    for i in range(100):
        betsize = 10
        players[1].playerStrategy(players[0].hand[0], shoe)
        if players[1].getValue() != -1:
            players[0].dealerStrategy(shoe)
            if players[0].getValue() > players[1].getValue():
                players[1].payout(-betsize) 
                betsize += betsize
            else:
                players[1].payout(betsize) 
                betsize = 10
        else:
            players[1].payout(-betsize) 
            betsize += betsize
        nextHand(players, shoe)
    print(players[1].stack)

if __name__ == "__main__":
    runGame()







