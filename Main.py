import pydealer as pd
from pydealer import tools
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

def createDeck(numberOfDecks):
    #probably need to overide the pydealer deck constructor
    deck = pd.Deck(rebuild=True, shuffle=True, ranks=BLACKJACK_RANKS)
    for i in range(numberOfDecks - 1):
        deck += tools.build_cards()
    return deck


def runGame(iterations, numberOfPlayers, numberOfDecks):
    shoe = createDeck(numberOfDecks)
    # we dont retain internal args when copying?
    shoe.rebuild = True
    shoe.re_shuffle = True
    shoe.shuffle(2)
    players = list() 

    winloss = 0
    startGame(players, numberOfPlayers, shoe)

    dealer = players[0]
    for i in range(iterations):
        for player in players[1:]:
            player.shouldSplit(dealer.hand[0], shoe)
            betsize = 10
            player.playerStrategy(dealer.hand[0], shoe)
            if player.getValue() != -1:
                dealer.dealerStrategy(shoe)
                if dealer.getValue() > player.getValue():
                    player.payout(-betsize) 
                    betsize += betsize
                else:
                    player.payout(betsize) 
                    betsize = 10
            else:
                player.payout(-betsize) 
                betsize += betsize
            if player.didWeSplit and player.getValue(True) != -1:
                if dealer.getValue() > player.getValue(True):
                    player.payout(-betsize) 
                    betsize += betsize
                else:
                    player.payout(betsize) 
                    betsize = 10
            else:
                player.payout(-betsize) 
                betsize += betsize
        nextHand(players, shoe)
    for player in players[1:]:
        print(player.stack)

if __name__ == "__main__":
    runGame(50, 2, 2)







