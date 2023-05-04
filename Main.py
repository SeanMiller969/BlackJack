import pydealer as pd
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
    #need to make it reshuffle the proper amount of cards.
    shoe.re_shuffle = True
    shoe.shuffle(2)
    players = list() 

    winloss = 0
    startGame(players, numberOfPlayers, shoe)

    dealer = players[0]
    buyin = 10
    for i in range(iterations):
        for player in players[1:]:
            player.shouldSplit(dealer.getDealerCard(), shoe)
            player.playerStrategy(dealer.getDealerCard(), shoe)
        dealer.dealerStrategy(shoe)
        for player in players[1:]:
            player.payout(buyin, dealer.getHandValue(dealer.getDealerHand()))
        nextHand(players, shoe)
    for player in players[1:]:
        print(player.stack)

if __name__ == "__main__":
    runGame(100, 2, 2)







