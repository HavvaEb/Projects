
from utils.game import Board

turn_count=0

Players_list = ['Akbar','Asghar','Moosa','Isa']
""" - the name and number of players is defined. 
    - I also import game from Board class."""

bs = Board(Players_list,turn_count)
res = 52 % len(Players_list)
num = 52-res
bw = int(num/len(Players_list))
for i in range (bw):
    bs.start_game()
    print("......................................")


