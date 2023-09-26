class Knight:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.board = None
        self.representation = " K"
        self.step_counter = 0

    def set_board(self, board):
        self.board = board
        if self.board.knight is not self:
            self.board.set_knight(self)

        # TODO:: Add moving instaed of setting
        self.board.area[self.x][self.y] = self.representation

    def move(self, coords):
        # Test possible moves.
        # If the move takes you closer to the edge use it?
        self.step_counter += 1
        self.board.area[self.x][self.y] = " " + str(self.step_counter)

        new_pos = (self.x+coords[0],  self.y+coords[1])
        self.x += new_pos[0]
        self.y += new_pos[1]
        self.board.area[new_pos[0]][new_pos[1]] = self.representation

    def find_move(self):
        # Possible moves (change of coords) of knight

        mv = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

        for move in mv:
            # TODO:: Evaluate the best possible move
            if (self.board.width >= (self.x + move[0])) and (self.board.height >= (self.y +
                                                                                                  move[1])):
                return move
        return None
