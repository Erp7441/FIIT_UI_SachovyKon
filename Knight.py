class Knight:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.board = None
        self.representation = " K"
        self.step_counter = 0
        self.moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

    def set_board(self, board):
        self.board = board
        if self.board.knight is not self:
            self.board.set_knight(self)

        # TODO:: Add moving instaed of setting
        self.board.area[self.x][self.y] = self.representation

    def move(self):

        # Mark current cell as visited
        self.step_counter += 1
        self.board.area[self.x][self.y] = " " + str(self.step_counter)

        # All of the cells are marked
        if self.check_board():
            return True

        # Try every possible move
        for move in self.moves:

            new_pos = (self.x+move[0],  self.y+move[1])
            if self.is_valid_move(new_pos[0], new_pos[1]):

                self.x = new_pos[0]
                self.y = new_pos[1]
                self.board.area[new_pos[0]][new_pos[1]] = self.representation
                self.board.print_board()

                if self.move():
                    return True

        self.board.area[self.x][self.y] = self.board.empty_cell
        return None

    def is_valid_move(self, x, y):
        return 0 <= x < len(self.board.area) and 0 <= y < len(self.board.area) and self.board.area[x][y] is self.board.empty_cell

    def check_board(self):
        return self.step_counter == len(self.board.area) ** 2
