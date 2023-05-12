import pydealer as pd
import blackJackDeck as bjd
from pydealer import tools
from player import Player
from const import *

def nextHand(hands, deck):
    for hand in hands:
        hand.clear()
        hand.add_card(2, deck, 0)

def startGame(hands, numberOfPlayers, deck):
    for i in range(numberOfPlayers + 1):
        hands.append(Player(pd.Stack()))
        hands[i].add_card(2, deck, 0)

def runGame(iterations, numberOfPlayers, numberOfDecks):
    shoe = bjd.BlackJackDeck(number_of_decks=numberOfDecks, rebuild=True, re_shuffle=True)
    shoe.shuffle(2)
    
    players = list() 

    winloss = 0
    startGame(players, numberOfPlayers, shoe)

    dealer = players[0]
    buyins = [ 10 for _ in range(0, numberOfPlayers) ]
    for _ in range(iterations):
        for player in players[1:]:
            player.shouldSplit(dealer.getDealerCard(), shoe)
            player.playerStrategy(dealer.getDealerCard(), shoe)
        dealer.dealerStrategy(shoe)
        index = 0
        for player in players[1:]:
            buyins[index] = player.payout(buyins[index], dealer.getHandValue(dealer.getDealerHand()))
            index += 1
            
        nextHand(players, shoe)

    for player in players[1:]:
        print(player.stack)

if __name__ == "__main__":
    runGame(200, 2, 2)







