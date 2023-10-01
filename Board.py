from Watchdog import Watchdog


class Board:
    def __init__(self, width, height):

        self.height = height
        self.empty_cell = 'x'  # Empty cell representation
        self.knight = None

        # If invalid width is entered. Set to chess default.
        if width > 0:
            self.width = width
        else:
            self.width = 8

        # If invalid height is entered. Set to chess default.
        if height > 0:
            self.height = height
        else:
            self.height = 8

        # Initializes 2D "empty" chessboard (array)
        self.area = [[self.empty_cell for _ in range(self.height)] for _ in range(self.width)]

    def set_knight(self, knight):
        self.knight = knight
        if self.knight.board is not self:
            self.knight.set_board(self)

    def start(self, timeout=50):
        self.print_board()

        watchdog = Watchdog(timeout)
        watchdog.start()
        if self.knight.start() is None:
            print("Game Over!")
        watchdog.stop()

        self.print_board()

    def print_board(self):
        for row in self.area:
            for col in row:
                print(" " * (10 - len(str(col))), end='')
                print(col, end='')
            print("\n", end='')
        print("----" * (len(self.area) + 1))
