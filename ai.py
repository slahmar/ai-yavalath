# Salomé Lahmar 16201438 

from position import Position
import sys
import constants

PATTERNS = {}
# Good patterns
PATTERNS["__ _"] = 5
PATTERNS["_ __"] = 5
PATTERNS[" __ _"] = 5
PATTERNS["_ __ "] = 5
PATTERNS[" _  _"] = 2 
PATTERNS["_  _ "] = 2
# Bad patterns
PATTERNS[" __ "] = -1
PATTERNS[" _ _ "] = -1

INFINITY = 100000
SIMPLE = 1
KILLER = 2
HISTORY = 3

class AI:
    def __init__(self):
        self.depth = None
        while self.depth == None:
            try:
                depth = input("Enter the depth of search : ")
                self.depth = int(depth)
            except ValueError:
                print("Please enter a number.")
        self.name = "the AI"
        self.piece = "O"

    def init_heuristics(self, pos):
        self.history_moves = {}
        self.killer_moves = {}
        for move in range(0,121):
            self.history_moves[move]=0
        for i in range(0, self.depth):
            self.killer_moves[i]= {}
            for move in range(0,121):
                self.killer_moves[i][move]=0
        
    def get_next_move(self, pos, last_move):
        for heuristic in (HISTORY, KILLER, SIMPLE):
            print(heuristic)
            self.heuristic = heuristic
            (move, value, static_eval) = self.alpha_beta_negamax(pos, self.depth-1)
            print("{} static evaluations".format(static_eval))
            self.print_move(move)
        return move

    def static_eval(self, pos):
        score = 0
        for pattern in PATTERNS:
            score += pos.find_pattern(pattern, PATTERNS[pattern], not pos.player)
            score -= pos.find_pattern(pattern, PATTERNS[pattern], pos.player)
        return score

    def alpha_beta_negamax(self, pos, depth, achievable = -INFINITY, hope = INFINITY, static_eval = 0):
        maxChild = None
        end = pos.end_game()
        if depth == 0 or end[0]:
            static_eval+=1
            if end[0]:
                if end[1] == pos.players[pos.player]:
                    eval = INFINITY
                elif end[0] == None:
                    eval = 0
                else:
                    eval = -INFINITY
            else:
                eval = self.static_eval(pos)
            return (None, eval, static_eval)
        else:
            moves = pos.available_moves()
            score = -INFINITY
            if self.heuristic == HISTORY:
                for move in moves:
                    moves[move] = self.history_moves[move]
            elif self.heuristic == KILLER:
                for move in moves:
                    moves[move] = self.killer_moves[depth-1][move]
            for child in sorted(moves, key=moves.get, reverse=True): 
                pos.make_move(child)    
                (result, temp, static_eval) = self.alpha_beta_negamax(pos, depth-1, -hope, -achievable, static_eval)
                temp = -temp
                pos.unmake_move(child)
                if temp >= hope:
                    if self.heuristic == HISTORY:
                        self.history_moves[child] += 1
                    elif self.heuristic == KILLER:
                        self.killer_moves[depth-1][child] += 1
                    return (child, temp, static_eval)
                if temp > achievable:
                    achievable = temp
                    maxChild = child
            if maxChild == None:
                maxChild = child
            return (maxChild, achievable, static_eval)

    def print_move(self, cell):
        rowInt = int(cell/11)-1
        rowString = chr(65+rowInt)
        column = cell%11
        if ord(rowString) >= 65 and ord(rowString) <= 69:
            column -= (11-constants.COLUMNS[rowString])-2
        print(self.name + " has played " +rowString+str(column))