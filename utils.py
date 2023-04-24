from const import BLACKJACK_RANKS

def val(card):
    return BLACKJACK_RANKS["values"].get(card.value)