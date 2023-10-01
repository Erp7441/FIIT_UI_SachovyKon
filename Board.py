class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.empty_cell = '\tx'  # Empty cell representation
        self.knight = None

        # Initializes 2D "empty" chessboard (array)
        self.area = [[self.empty_cell for i in range(self.height)] for j in range(self.width)]

    def set_knight(self, knight):
        self.knight = knight
        if self.knight.board is not self:
            self.knight.set_board(self)

    def start(self):
        self.print_board()

        if self.knight.start() is None:
            print("Game Over!")

        self.print_board()

    def print_board(self):
        for row in self.area:
            for col in row:
                print(col, end='')
            print("\n", end='')
        print("________________________________________________________________________________________________________________________________")
