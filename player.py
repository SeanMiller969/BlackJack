from const import *
import utils

class Player:
    def __init__(self, hand):
        self.hand = hand
        self.stack = 1000

    def getValue(self):
        amount = 0
        self.hand.sort(ranks=BLACKJACK_RANKS)
        for card in self.hand:
            amount += utils.val(card)
            if amount > 21 and utils.val(card) == 11:
                amount -= 11 
                amount += 1
        return amount if amount < 21 else -1

    def payout(self, amount):
        self.stack += amount
        
    def clear(self):
        self.hand.empty()

    def add_card(self, num, deck):
        self.hand += deck.deal(num)
    
    def split(self):
        return
    
    def doubleDown(self):
        return

    def dealerStrategy(self, deck):
        while self.getValue() < 17 and self.getValue() != -1:
            self.add_card(1, deck)
        return self.getValue()

    def playerStrategy(self, dealerCard, deck):
        while self.getValue() != -1 and RANGES["default"][(utils.val(dealerCard), self.getValue())] != 0:
            self.add_card(1, deck)
        return self.getValue()
