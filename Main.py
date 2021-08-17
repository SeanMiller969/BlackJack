import random
import numpy

#black jack simple optmific simulation
#main algorithim
#optimific play
#card counting for bet size
#card counting for resuffle
#calculate win loss

Values = ["two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "jack", "queen", "king", "ace"]

Suits = ["H", "S", "C", "D"]

class Card:
    def __init__(self, face, suit):
        self.f = face
        self.s = suit
    
    def getCard(self):
        return (self.f, self.s)

    def getValue(self):
        if (self.f == "one"):
            return 1
        if (self.f == "two"):
            return 2
        if (self.f == "three"):
            return 3
        if (self.f == "four"):
            return 4
        if (self.f == "five"):
            return 5
        if (self.f == "six"):
            return 6
        if (self.f == "seven"):
            return 7
        if (self.f == "eight"):
            return 8
        if (self.f == "nine"):
            return 9
        if (self.f == "ten"):
            return 10
        if (self.f == "ace"):
            return (11, 1)
        return 10
    
    def printCard(self):
        print(self.s + "-----" + self.s)
        print("|" + self.f + (5 - len(self.f)) * " " +  "|")
        print("|" + self.f + (5 - len(self.f)) * " " +  "|")
        print("|" + self.f + (5 - len(self.f)) * " " +  "|")
        print(self.s + "-----" + self.s)

class Deck:
    def __init__(self, numberofdecks):
        self.n = numberofdecks
        self.deck = []
        for i in range(numberofdecks):
            for suit in Suits:
                for face in Values:
                    self.deck.append(Card(face, suit))
        print(len(self.deck))
                    
    def printDeck(self):
        for val in self.deck:
            print(val.getCard())
    
    def shuffleDeck(self):
        i = 0
        swaps = random.randrange(1000, 1200)
        while i < swaps:
            num1 = random.randrange(0, 52 * self.n)
            num2 = random.randrange(0, 52 * self.n)
            tmp = self.deck[num1] 
            self.deck[num1] = self.deck[num2]
            self.deck[num2] = tmp
            i += 1

class Player:
    def __init__(self, hand):
        self.hand = hand

class Dealer:
    def __init__(self, hand):
        self.hand = hand
        

if __name__ == "__main__":
    shoe = Deck(1)
    shoe.shuffleDeck()

    
    












