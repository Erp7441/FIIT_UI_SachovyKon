class Knight:

    def __init__(self, position):
        self.position = position
        self.board = None

    def set_board(self, board):
        self.board = board
        if self.board.knight is not self:
            self.board.set_knight(self)

    def move(self):
        # Test possible moves.
        # If the move takes you closer to the edge use it?
        pass

    def find_move(self):
        # Possible moves (change of coords) of knight

        mv = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

        for movement in mv:
            pass

        pass
