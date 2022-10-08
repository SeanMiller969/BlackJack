import random
#import numpy

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
            return 11
        return 10
    
    def printCard(self):
        print(self.s + "-----" + self.s)
        print("|" + self.f + (5 - len(self.f)) * " " +  "|")
        print("|" + self.f + (5 - len(self.f)) * " " +  "|")
        print("|" + self.f + (5 - len(self.f)) * " " +  "|")
        print(self.s + "-----" + self.s)

    def outside(self):
        print(self.s + "-----" + self.s, end="")
    
    def inside(self):
        print("|" + self.f + (5 - len(self.f)) * " " +  "|", end="")

class Deck:
    def __init__(self, numberofdecks):
        self.n = numberofdecks
        self.deck = []
        for i in range(numberofdecks):
            for suit in Suits:
                for face in Values:
                    self.deck.append(Card(face, suit))
                    
    def printDeck(self):
        for val in self.deck:
            print(val.getCard())

    def deal(self):
        return self.deck.pop()

    def cardsLeft(self):
        return len(self.deck)
            
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
    def __init__(self, usershand):
        self.hand = usershand
        self.wins = 0
        self.losses = 0

    def getValue(self):
        self.hand.sort(key=lambda x: x.getValue())
        amount = 0
        for card in self.hand:
            amount += card.getValue()
            if amount > 21 and card.getValue() == 11:
                amount -= 11 
                amount += 1
        if amount > 21:
            return -1
        else:
            return amount    

    def firstCardValue(self):
        return self.hand[0].getValue()

    def hit(self, card):
        self.hand.append(card)

    def win(self):
        self.wins += 1

    def lose(self):
        self.losses += 1

    def winloss(self):
        return float(self.wins) / float(self.wins + self.losses)

    def printHand(self):
        for card in self.hand:
            card.outside()
            print(" ", end=" ")
        print("")
        for i in range(0, 3):
            for card in self.hand:
                card.inside()
                print(" ", end=" ")
            print("")
        for card in self.hand:
            card.outside()
            print(" ", end=" ")
        print("")
    
    def dealerPlay(self, shoe):
        while True:
            if self.getValue() == -1:
                break
            elif self.getValue() < 17:
                self.hit(shoe.deal())
            else:
                break
    
    def playerStratOptimalPlay(self, shoe, dealerCardValue): 
        while(True):
            if self.getValue() == -1:
                return
            elif self.getValue() >= 17:
                return
            elif dealerCardValue <= 6 and self.getValue() > 11:
                return
            else:
                self.hit(shoe.deal())



    def reset(self):
        self.hand = list()

if __name__ == "__main__":
    shoe = Deck(1)
    shoe.shuffleDeck()

    
    
    hand = list()
    hand.append(shoe.deal())
    hand.append(shoe.deal())
    player = Player(hand)
    
    dealerHand = list()
    dealerHand.append(shoe.deal())
    dealerHand.append(shoe.deal())
    dealer = Player(dealerHand)


    '''
    for player in table:
        while True:
            player.printHand()
            print(player.getValue())
            if player.getValue() == 21:
                print("You Win")
                exit()
            decision = input("hit or stand: ")
            if decision == "hit":
                player.hit(shoe.deal())
                if player.getValue() == -1:
                    player.printHand()
                    print("Busted")
                    exit()
            elif decision == "stand":
                break

    '''


    
    for i in  range(0, 1000000):
        player.playerStratOptimalPlay(shoe, dealer.firstCardValue())
        if player.getValue() != -1:
            dealer.dealerPlay(shoe)
            if player.getValue() > dealer.getValue():
                player.win()
                dealer.lose()
            else:
                player.lose()
                dealer.win()
        else:
            dealer.win()
            player.lose()

        if shoe.cardsLeft() < 14:
            shoe = Deck(1)
            shoe.shuffleDeck()
        player.reset()
        player.hit(shoe.deal())
        player.hit(shoe.deal())
        dealer.reset()
        dealer.hit(shoe.deal())
        dealer.hit(shoe.deal())
    
    print(dealer.winloss())
    













