from utils.card import Card
import random


class Player:
    """class Player that contains these attributes:
       -cards: which is a list of Card. (you will need to import Card from card.py). In a real card game, this is equivalent to the cards that the player has in his hands.
       -turn_count: which is an int starting a 0.
       -history: which is a list of Card that will contain all the cards played by the player."""
    def __init__(self, cards) -> None:
        self.cards = cards
        self.history = []
        self.turn_count = 0

    def __iter__(self):
        """ returns an iterator for the given object """
        for i in self.cards:
            yield i

    def play(self):
        """- randomly pick a Card in cards.
           - Add the Card to the Player's history.
           - Return the Card"""
        random_card = self.cards.pop()
        self.history.append(random_card)
        return random_card  


   
class Deck:
    """class Player that contains these attributes and methods:
       - An attribute cards: which is going to contain a list of instances of Card.
       - A fill_deck() method that will fill cards with a complete card game 
       - A shuffle() method that will shuffle all the list of cards.
       - A distribute2() that will take a list of Player as parameter and will distribute the cards between all the players."""
    def __init__(self):
        self.hands = []
        self.cards = []
        self.fill_deck()
    def fill_deck(self): 
        for i in range(4):
            for j in range(13):
                if i < 2:
                    self.cards.append(Card(0, i, j))
                else:
                    self.cards.append(Card(1, i, j))

    def __iter__(self):
        """ returns an iterator for the given object """
        for i in self.hands:
            yield i

    def shuffle(self):
        random.shuffle(self.cards)
        
    def distribute2(self,name_players):
        n_players = len(name_players)
        res = 52 % n_players
        num = 52-res
        pnum = int(num/n_players)
        for i in range(pnum):
            self.hands.append(self.cards.pop())
                 
    def __str__(self):
        """Method called during a conversion of the object into a chain"""
        return f"{self.cards}"
