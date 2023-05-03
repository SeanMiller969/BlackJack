from const import *
import utils

class Player:
    def __init__(self, hand):
        self.hands = list()
        self.hands.append(hand)
        self.didWeDoubleDown = False
        self.stack = 1000

    def getDealerCard(self):
        return self.hands[0][0]

    def payout(self, amount, dealerValue):
        for hand in self.hands:
            if utils.getHandValue(hand) == -1 or utils.getHandValue(hand) < dealerValue:
                self.stack += -amount
            elif utils.getHandValue(hand) == dealerValue:
                continue
            else:
                self.stack += amount 

    def clear(self):
        self.hands[0].empty()
        while len(self.hands) != 1:
            self.hands.pop()

    def hasAce(self, hand):
        return False if utils.val(hand[0]) != 11 and utils.val(hand[1]) != 11 else True

    def add_card(self, num, deck, index):
        self.hands[index] += deck.deal(num)
    
    def shouldSplit(self, dealerCard, deck):
        #if player has two equal cards then they can split their hand
        if self.hands[0][0].value == self.hands[0][1].value and RANGES["splitRange"][(utils.val(dealerCard), utils.val(self.hands[0][0]))]:
            tmp = self.hands[0].split()
            self.hands[0] = tmp[0]
            self.add_card(1, deck, 0)
            self.hands.append(tmp[1])
            self.add_card(1, deck, 1)
        else:
            self.didWeSplit = False
    
    def doubleDown(self, deck, betsize):
        #check double down range
        self.add_card(1, deck, 0)
        return betsize * 2

    def dealerStrategy(self, deck):
        #dealer always hits unless at 17
        while utils.getHandValue(self.hands[0]) < 17 and utils.getHandValue(self.hands[0]) != -1:
            self.add_card(1, deck, 0)

    def playerStrategy(self, dealerCard, deck):
        #go through hands determine if hit or stand 
        for index in range(len(self.hands)):
            whatRange = "Soft Ace" if self.hasAce(self.hands[index]) else "default"
            while utils.getHandValue(self.hands[index]) != -1 and RANGES[whatRange][(utils.val(dealerCard), 
                                                                                     utils.getHandValue(self.hands[index]) - 11 
                                                                                     if whatRange == "Soft Ace" else utils.getHandValue(self.hands[index]))] != 0:
                self.add_card(1, deck, index)
                whatRange = "default"
