
#===============================================================================
# Blackjack card values
#===============================================================================

BLACKJACK_RANKS = {
    "values": {
        "Ace": 11,
        "King": 10,
        "Queen": 10,
        "Jack": 10,
        "10": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 5,
        "2": 2
    }
}

#===============================================================================
# Blackjack ranges
#===============================================================================

#manually selcting probably a better way
#1 == hit 0 == stand
RANGES = {
    "default": {
        (2, 4): 1,
        (2, 5): 1,
        (2, 6): 1,
        (2, 7): 1,
        (2, 8): 1,
        (2, 9): 1,
        (2, 10): 1,
        (2, 11): 1,
        (2, 12): 1,
        (2, 13): 0,
        (2, 14): 0,
        (2, 15): 0,
        (2, 16): 0,
        (2, 17): 0,
        (2, 18): 0,
        (2, 19): 0,
        (2, 20): 0,
        (2, 21): 0,
        (3, 4): 1,
        (3, 5): 1,
        (3, 6): 1,
        (3, 7): 1,
        (3, 8): 1,
        (3, 9): 1,
        (3, 10): 1,
        (3, 11): 1,
        (3, 12): 1,
        (3, 13): 0,
        (3, 14): 0,
        (3, 15): 0,
        (3, 16): 0,
        (3, 17): 0,
        (3, 18): 0,
        (3, 19): 0,
        (3, 20): 0,
        (3, 21): 0,
        (4, 4): 1,
        (4, 5): 1,
        (4, 6): 1,
        (4, 7): 1,
        (4, 8): 1,
        (4, 9): 1,
        (4, 10): 1,
        (4, 11): 1,
        (4, 12): 0,
        (4, 13): 0,
        (4, 14): 0,
        (4, 15): 0,
        (4, 16): 0,
        (4, 17): 0,
        (4, 18): 0,
        (4, 19): 0,
        (4, 20): 0,
        (4, 21): 0,
        (5, 4): 1,
        (5, 5): 1,
        (5, 6): 1,
        (5, 7): 1,
        (5, 8): 1,
        (5, 9): 1,
        (5, 10): 1,
        (5, 11): 1,
        (5, 12): 0,
        (5, 13): 0,
        (5, 14): 0,
        (5, 15): 0,
        (5, 16): 0,
        (5, 17): 0,
        (5, 18): 0,
        (5, 19): 0,
        (5, 20): 0,
        (5, 21): 0,
        (6, 4): 1,
        (6, 5): 1,
        (6, 6): 1,
        (6, 7): 1,
        (6, 8): 1,
        (6, 9): 1,
        (6, 10): 1,
        (6, 11): 1,
        (6, 12): 0,
        (6, 13): 0,
        (6, 14): 0,
        (6, 15): 0,
        (6, 16): 0,
        (6, 17): 0,
        (6, 18): 0,
        (6, 19): 0,
        (6, 20): 0,
        (6, 21): 0,
        (7, 4): 1,
        (7, 5): 1,
        (7, 6): 1,
        (7, 7): 1,
        (7, 8): 1,
        (7, 9): 1,
        (7, 10): 1,
        (7, 11): 1,
        (7, 12): 1,
        (7, 13): 1,
        (7, 14): 1,
        (7, 15): 1,
        (7, 16): 1,
        (7, 17): 0,
        (7, 18): 0,
        (7, 19): 0,
        (7, 20): 0,
        (7, 21): 0,
        (8, 4): 1,
        (8, 5): 1,
        (8, 6): 1,
        (8, 7): 1,
        (8, 8): 1,
        (8, 9): 1,
        (8, 10): 1,
        (8, 11): 1,
        (8, 12): 1,
        (8, 13): 1,
        (8, 14): 1,
        (8, 15): 1,
        (8, 16): 1,
        (8, 17): 0,
        (8, 18): 0,
        (8, 19): 0,
        (8, 20): 0,
        (8, 21): 0,
        (9, 4): 1,
        (9, 5): 1,
        (9, 6): 1,
        (9, 7): 1,
        (9, 8): 1,
        (9, 9): 1,
        (9, 10): 1,
        (9, 11): 1,
        (9, 12): 1,
        (9, 13): 1,
        (9, 14): 1,
        (9, 15): 1,
        (9, 16): 1,
        (9, 17): 0,
        (9, 18): 0,
        (9, 19): 0,
        (9, 20): 0,
        (9, 21): 0,
        (10, 4): 1,
        (10, 5): 1,
        (10, 6): 1,
        (10, 7): 1,
        (10, 8): 1,
        (10, 9): 1,
        (10, 10): 1,
        (10, 11): 1,
        (10, 12): 1,
        (10, 13): 1,
        (10, 14): 1,
        (10, 15): 1,
        (10, 16): 1,
        (10, 17): 0,
        (10, 18): 0,
        (10, 19): 0,
        (10, 20): 0,
        (10, 21): 0,
        (11, 4): 1,
        (11, 5): 1,
        (11, 6): 1,
        (11, 7): 1,
        (11, 8): 1,
        (11, 9): 1,
        (11, 10): 1,
        (11, 11): 1,
        (11, 12): 1,
        (11, 13): 1,
        (11, 14): 1,
        (11, 15): 1,
        (11, 16): 1,
        (11, 17): 0,
        (11, 18): 0,
        (11, 19): 0,
        (11, 20): 0,
        (11, 21): 0,
    }
}
