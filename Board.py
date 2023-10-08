from Watchdog import Watchdog


class Board:
    def __init__(self, width=8, height=8):

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
        result = self.knight.start()
        watchdog.stop()

        if result is None:
            print("Game Over!")
            return False

        self.print_board()
        return True

    def print_board(self):
        for row in self.area:
            for col in row:
                print(" " * (10 - len(str(col))), end='')
                print(col, end='')
            print("\n", end='')
        dash_count = int(len(self.area) * 2 + len(self.area) / 2) + 3
        print("----" * dash_count)
