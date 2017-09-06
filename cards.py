import random
import pprint

# Teacher Example
class Deck(object):
    def __init__(self):
        self.deck = []
        self.reset()
        self.shuffle()
    
    def reset(self):
        self.deck = [] 
        suits = ['Spades','Hearts','Clubs','Diamonds']
        pips = ['Ace','2','3','4','5','6','7','8','9','10','J','Q','K']

        for suit in range (0,len(suits)):
            for pip in range(0,len(pips)):
                self.deck.append([pips[pip]] + " of " + suits[suit])
        return self 

    def shuffle(self):
        random.shuffle(self.deck)
        return self 

    def deal(self):
        return self.deck.pop()

class Player(object):
    def __init__(self,name):
        self.name = nameself.hand = []

    def draw(self,deck):
        pass
        
    def discard():
        self.hand = []
        return self 

class Card(object):
    def __init__(self,pip,suit):
        self.pip = pip
        self.suit = suit 

deck3 = Deck()
player2 = Player('Keith')
player2.draw(deck3).draw(deck3)
pprint.pprint(player2.hand

# class Deck(object):
#     def __init__(self):
#         vals = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
#         self.deck = []
#         for ind in vals: 
#             self.deck.append([ind,"S"])
#             self.deck.append([ind,"D"])
#             self.deck.append([ind,"C"])
#             self.deck.append([ind,"H"]) 

# class Player(object):
#     def shuffle(self,cards):
#         print "shuffling"
#         print cards
#         self.shuffled = random.shuffle(cards)
#         print self.shuffled
#         return self 

# deck1 = Deck()
# card = deck1.deck
# player1 = Player()
# print player1.shuffle(card)