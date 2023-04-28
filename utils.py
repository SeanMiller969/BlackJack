from const import BLACKJACK_RANKS

def val(card):
    return BLACKJACK_RANKS["values"].get(card.value)

def getHandValue(hand):
    amount = 0
    hand.sort(ranks=BLACKJACK_RANKS) 
    for card in hand:
        amount += val(card)
        if amount > 21 and val(card) == 11:
            amount -= 11 
            amount += 1
    return amount if amount < 21 else -1