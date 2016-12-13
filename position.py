# Salomé Lahmar 16201438
PRINTABLE = [0,0,0,0,0,1,3,3,3,3,2,
        0,0,0,0,5,7,7,7,7,7,2,
        0,0,0,5,7,7,7,7,7,7,2,
        0,0,5,7,7,7,7,7,7,7,2,
        0,5,7,7,7,7,7,7,7,7,2,
        4,7,7,7,7,7,7,7,7,7,0,
        4,7,7,7,7,7,7,7,7,0,0,
        4,7,7,7,7,7,7,7,0,0,0,
        4,7,7,7,7,7,7,0,0,0,0,
        4,7,7,7,7,7,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0]

PLAYABLE = [0,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,1,1,1,1,1,0,
    0,0,0,0,1,1,1,1,1,1,0,
    0,0,0,1,1,1,1,1,1,1,0,
    0,0,1,1,1,1,1,1,1,1,0,
    0,1,1,1,1,1,1,1,1,1,0,
    0,1,1,1,1,1,1,1,1,0,0,
    0,1,1,1,1,1,1,1,0,0,0,
    0,1,1,1,1,1,1,0,0,0,0,
    0,1,1,1,1,1,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0]

HORIZONTAL = 1
VERTICAL = 10
DIAGONAL = 11

class Position:
    def __init__(self, players): 
        board = []
        for i in range(0, 121):
            if PLAYABLE[i] == 1:
                board.append(" ")
            else:
                board.append("-")
        self.position = board
        self.players = players;
        self.player = 0
        self.moves_played = 0
        self.own_move = False

    def make_move(self, cell):
        self.player = not self.player
        if self.moves_played == 1 and self.position[cell] != " ":
            self.own_move = True
        self.moves_played+=1
        self.position[cell] = self.players[self.player].piece

    def unmake_move(self, cell):
        self.player = not self.player
        if self.moves_played == 2 and self.own_move == True:
            self.position[cell] = self.players[self.player].piece
            self.own_move = False
        else:
            self.position[cell] = " "
        self.moves_played-=1

    def available_moves(self):
        moves = {}
        for cell in range(0, 121):
            if self.position[cell] == " ":
                moves[cell] = 0
            elif self.moves_played == 1 and self.position[cell] != "-":
                moves[cell] = 0
        return moves

    def end_game(self):
        max_aligned = 0
        end = self.find_pattern("____", 1, self.player)
        if end > 0:
            return (True, self.players[not self.player])
        elif end == 0:
            end = self.find_pattern("___", 1, self.player)
            if end > 0:
                return (True, self.players[self.player])
            elif end == 0:
                if (not self.own_move and self.moves_played == 61) or (self.own_move and self.moves_played == 62):
                    return (True, None)
                else:
                    return (False, None)


    def find_pattern(self, pattern, rate, player):
        pattern = pattern.replace("_", self.players[player].piece)
        score = 0
        occurrences = self.number_horizontal_occurrences(pattern)
        occurrences += self.number_vertical_occurrences(pattern, VERTICAL)
        occurrences += self.number_vertical_occurrences(pattern, DIAGONAL)
        score += occurrences*rate
        return score

    def number_horizontal_occurrences(self, pattern):
        occurrences = 0
        seg = ""
        for i in range(0, 121):
            if self.position[i] != "-":
                seg += self.position[i]
            else :
                occurrences += seg.count(pattern)
                seg = ""
        return occurrences

    def number_vertical_occurrences(self, pattern, direction):
        occurrences = 0
        for i in range (0, direction):
            seg = ""
            for j in range (i, 121, direction):
                if self.position[j] != "-":
                    seg += self.position[j]
            occurrences += seg.count(pattern)
        return occurrences

    def print_board(self, end = (False, None)):
        indent = 0;
        printing = "";
        for row_index in range(0,11) :
            row = [self.position[i] for i in range(row_index*11, row_index*11+11)]
            for i in range(0,indent) :
                printing+=" "
            cell_index = 0
            for cell in row :
                if PLAYABLE[row_index*11+cell_index] == 1 :
                    printing += str(cell)
                else:
                    printing+= " "
                printing += " "
                if PRINTABLE[row_index*11+cell_index] in (4,5,7):
                    printing+="|"
                else:
                    printing+=" "
                printing+= " "
                cell_index+=1
            printing+= "\n"
            for i in range(0,indent-1) :
                printing+= " "
            cell_index = 0
            for cell in row:
                if PRINTABLE[row_index*11+cell_index] in (2,3,7):
                    printing+="\\"
                elif PRINTABLE[row_index*11+cell_index] == 1:
                    printing+=""
                else:
                    printing+=" "
                printing+= " "
                if PRINTABLE[row_index*11+cell_index] in (1,3,5,7):
                    printing+="/"
                else:
                    printing+=" "
                printing+=" "
                cell_index+=1
            printing+="\n"
            indent+=2

        print(printing)
        if end[0]:
            if end[1] != None:
                print("{} has won the game.".format(end[1].name))
            else:
                print("This is a draw.")
        else:
            print("This is {}'s turn to play now.".format(self.players[self.player].name))
