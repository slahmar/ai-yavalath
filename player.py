# Salomé Lahmar 16201438
import constants

class Player:
    def __init__(self):
        self.name = input("Enter your name : ")
        self.piece = "X"

    def get_next_move(self, pos, last_move):
        to_return = None
        while to_return == None:
            move = input("Enter your move : ")
            if len(move) == 2:
                row = move[0]
                if ord(row) >= 65 and ord(row) <= 73:
                    try:
                        column_string = move[1]
                        column = int(column_string)
                        if column in range(1, constants.COLUMNS[row]+1):
                            cell = self.translate_to_cell(row, column)
                            if pos.position[cell] == " ":
                                to_return = cell
                            else :
                                print("This cell is already occupied. Please enter another move.")
                        else:
                            print("No such playable cell exists.")
                    except ValueError:
                        print("Wrong syntax.")
                else:
                    print("No such playable cell exists.")
            elif move == "X":
                if pos.moves_played == 1 :
                    pos.own_move = True
                    self.make_move(pos, last_move)
                else:
                    print("This move is only allowed as the second move of the game.")
            else:
                print("Wrong syntax.")
        return to_return

    def translate_to_cell(self, row, column):
        cell = (ord(row)-65+1)*11-1 # end of previous row
        if ord(row) >= 65 and ord(row) <= 69:
            cell += (11-constants.COLUMNS[row]-1)+column
        else:
            cell+= 1+column
        return cell
