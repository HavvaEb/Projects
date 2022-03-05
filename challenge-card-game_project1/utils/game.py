from utils.card import Card
from utils.player import Player
from utils.player import Deck

class Board():
    """A class called Board that contains:
      - An attribute players that is a list of Player. 
      - number of players.
      - An attribute turn_count that is an int.
      - An attribute active_cards that will contain a list of card played.
      - An attribute history_cards that will contain all the cards played since the start of the game, except for active_cards.
"""
    def __init__(self, Players: 'list[str]',turn_count: int) -> None:
        self.Players = Players
        self.numberp = len(Players)
        self.PP = []
        self.turn_count = turn_count
        self.active_cards = []
        self.history=[]
        self.mycard = []

    
    def start_game(self):
        """A method start_game() that will:
           - print Game started...,
           - Fill a Deck,
           - Distribute the cards of the Deck to the player
           - Make each Player play() a Card, where each player should only play 1 card per turn, and all players have to play at each turn until they have no cards left.
           - At the end of each turn print:
              -The turn count.
              -The list of active cards.
              -The number of cards in the history_cards."""
              
        print("Game starts...")
        dc = Deck()
        dc.shuffle()
        for i in range(self.numberp):
            dc.distribute2(self.Players)


        for card3 in dc:
            self.mycard.append(str(card3))

        self.turn_count = self.turn_count+1
        print("Turn count is {}:".format(self.turn_count))
        
        res = 52 % self.numberp
        num = 52-res
        bw = int(num/self.numberp)

        for i in range(self.numberp):
            cc = self.mycard[i*bw:(i+1)*bw]
            self.PP.append(cc)

        for i in range(self.numberp):
            pc = Player(self.PP[i])
            
            print("{} played card:".format(self.Players[i]))
            vv= pc.play()
            print(vv)
            self.history.append(vv)

            print("History of played card {}:".format(self.history))

        if (self.turn_count==bw):
            print("Game Over......................................................")
            

            


  
