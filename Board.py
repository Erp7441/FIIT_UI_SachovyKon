class Board:
    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.area = [['*'] * self.dimensions[0]] * self.dimensions[1]
        self.knight = None

    def set_knight(self, knight):
        self.knight = knight
        if self.knight.board is not self:
            self.knight.set_board(self)

    def start(self):
        # TODO:: Change condition to if the board has not been fully walked thru
        while True:
            self.knight.move()
            self.print_board()

    def print_board(self):
        for row in self.area:
            for col in row:
                print(col, end='')
            print("\n", end='')
        print("________________________________")