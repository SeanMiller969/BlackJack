import pydealer as pd
import blackJackDeck as bjd
from pydealer import tools
from player import Player
import matplotlib.pyplot as plt
import numpy as np
from const import *

playerStacks = [[] for i  in range(0, 2)]
playerBetSize = [[] for i  in range(0, 2)]

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
            print(buyins[index])
            buyins[index] = player.payout(buyins[index], dealer.getHandValue(dealer.getDealerHand()))
            playerStacks[index].append(players[index + 1].stack)
            playerBetSize[index].append(buyins[index])
            index += 1
            
        nextHand(players, shoe)
        
    for player in players[1:]:
        print(player.stack)

if __name__ == "__main__":
    runGame(200, 2, 2)
    fig, ax = plt.subplots()
    x = np.arange(0, 200)    
    ax.plot(x, playerStacks[0], color = 'green', linewidth=2.0)
    ax.plot(x, playerStacks[1], color = 'red', linewidth=2.0)
    plt.show()







