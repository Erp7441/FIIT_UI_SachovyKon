from time import sleep
from Constants import Constants


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.empty_cell = '[]'
        self.area = [[self.empty_cell for i in range(self.height)] for j in range(self.width)]
        self.knight = None

    def set_knight(self, knight):
        self.knight = knight
        if self.knight.board is not self:
            self.knight.set_board(self)

    def start(self):
        # TODO:: Change condition to if the board has not been fully walked thru
        self.print_board()

        while self.check_board():
            valid_move = self.knight.find_move()
            if valid_move != None:
                self.knight.move(valid_move)
                self.print_board()
                sleep(Constants.wait_time)
            else:
                print ("Game finished")
                return

    def print_board(self):
        for row in self.area:
            for col in row:
                print(col, end='')
            print("\n", end='')
        print("________________________________")

    def check_board(self):
        return True
