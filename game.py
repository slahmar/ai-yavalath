# Salomé Lahmar 16201438

from position import Position
from ai import AI
from player import Player

class Game:

    def __init__(self):
        player1 = Player()
        player2 = AI()
        self.players = [player1, player2]
        self.pos = Position(self.players)
        player2.init_heuristics(self.pos)
        self.pos.print_board()
        self.last_move = None

    def play_game(self):
        end = (False, None)
        while end[0] == False: 
            for player in self.players:
                move = player.get_next_move(self.pos, self.last_move)
                end = self.make_move(move)
                last_move = move
                if end[0]:
                    break
        print("Thanks for playing !")

    def make_move(self, cell):
        self.pos.make_move(cell)    
        end = self.pos.end_game()
        self.pos.print_board(end)
        return end