from const import *

class Player:
    def __init__(self, hand):
        self.hands = list()
        self.hands.append(hand)
        self.didWeDoubleDown = False
        self.pervBetSize = 10
        self.stack = 1000

    def getDealerCard(self):
        return self.hands[0][0]
    
    def getDealerHand(self):
        return self.hands[0]
    
    def val(self, card):
        return BLACKJACK_RANKS["values"].get(card.value)

    def getHandValue(self, hand):
        amount = 0
        hand.sort(ranks=BLACKJACK_RANKS) 
        for card in hand:
            amount += self.val(card)
            if amount > 21 and self.val(card) == 11:
                amount -= 11 
                amount += 1
        return amount if amount < 21 else -1

    def payout(self, amount, dealerValue):
        loss = False
        for hand in self.hands:
            if self.getHandValue(hand) == -1 or self.getHandValue(hand) < dealerValue:
                self.stack += -amount
                loss = True
            elif self.getHandValue(hand) == dealerValue:
                continue
            else:
                self.stack += amount 
        
        if loss:
            newAmount = amount + self.pervBetSize
            self.pervBetSize = amount
            return newAmount
        
        return 10

    def clear(self):
        self.hands[0].empty()
        while len(self.hands) != 1:
            self.hands.pop()

    def hasAce(self, hand):
        return True if (self.val(hand[0]) == 11) ^ (self.val(hand[1]) == 11) else False

    def add_card(self, num, deck, index):
        self.hands[index] += deck.deal(num)
    
    def shouldSplit(self, dealerCard, deck):
        #if player has two equal cards then they can split their hand
        if self.hands[0][0].value == self.hands[0][1].value and RANGES["splitRange"][(self.val(dealerCard), self.val(self.hands[0][0]))]:
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
        while self.getHandValue(self.hands[0]) < 17 and self.getHandValue(self.hands[0]) != -1:
            self.add_card(1, deck, 0)

    def playerStrategy(self, dealerCard, deck):
        #go through hands determine if hit or stand 
        for index in range(len(self.hands)):
            whatRange = "Soft Ace" if self.hasAce(self.hands[index]) else "default"
            while self.getHandValue(self.hands[index]) != -1 and RANGES[whatRange][(self.val(dealerCard), 
                                                                                     self.getHandValue(self.hands[index]) - 11 
                                                                                     if whatRange == "Soft Ace" else self.getHandValue(self.hands[index]))] != 0:
                self.add_card(1, deck, index)
                whatRange = "default"
