from const import *
import utils

class Player:
    def __init__(self, hand):
        self.hand = hand
        self.splithand = hand
        self.didWeSplit = False
        self.didWeDoubleDown = False
        self.stack = 1000

    def getValue(self, split=False):
        amount = 0
        self.hand.sort(ranks=BLACKJACK_RANKS) 
        self.splithand.sort(ranks=BLACKJACK_RANKS)
        for card in self.hand if not split else self.splithand:
            amount += utils.val(card)
            if amount > 21 and utils.val(card) == 11:
                amount -= 11 
                amount += 1
        return amount if amount < 21 else -1

    def payout(self, amount):
        self.stack += amount
        
    def clear(self):
        self.hand.empty()

    def add_card(self, num, deck, split=False):
        if not split:
            self.hand += deck.deal(num)
        else:
            self.splithand += deck.deal(num)
    
    def shouldSplit(self, dealerCard, deck):
        if self.hand[0].value == self.hand[1].value and RANGES["splitRange"][(utils.val(dealerCard), utils.val(self.hand[0]))]:
            tmp = self.hand.split()
            self.hand = tmp[0]
            self.add_card(1, deck)
            self.splithand = tmp[1]
            self.add_card(1, deck, True)
            self.didWeSplit = True
        else:
            self.didWeSplit = False
    
    def doubleDown(self):
        return

    def dealerStrategy(self, deck):
        while self.getValue() < 17 and self.getValue() != -1:
            self.add_card(1, deck)
        return self.getValue()

    def playerStrategy(self, dealerCard, deck):
        while self.getValue() != -1 and RANGES["default"][(utils.val(dealerCard), self.getValue())] != 0:
            self.add_card(1, deck)

        if self.didWeSplit:
            while self.getValue(True) != -1 and RANGES["default"][(utils.val(dealerCard), self.getValue(True))] != 0:
                self.add_card(1, deck, True)

        return self.getValue()
