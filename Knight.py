class Knight:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.board = None
        self.representation = "\tK"
        self.step_counter = 0
        self.moves = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]

    def set_board(self, board):
        self.board = board
        if self.board.knight is not self:
            self.board.set_knight(self)

        # TODO:: Add moving instaed of setting
        self.board.area[self.x][self.y] = self.representation

    def move(self, coords: tuple):
        self.x = coords[0]
        self.y = coords[1]
        self.board.area[self.x][self.y] = self.representation

    def start(self):
        self.step_counter += 1

        if Knight.find_path(self.x, self.y, self.board, self.step_counter, self):
            return True

    @staticmethod
    def find_path(x, y, board,step_counter, figure):
        # All the cells are marked
        if step_counter == len(board.area) ** 2:
            return True

        # Try every possible move
        for move_x, move_y in figure.moves:
            new_pos_x, new_pos_y = x+move_x,  y+move_y
            if figure.is_valid_move(new_pos_x, new_pos_y):

                board.area[x][y] = "\t" + str(step_counter)
                figure.move((new_pos_x, new_pos_y))

                if Knight.find_path(new_pos_x, new_pos_y, board, step_counter+1, figure):
                    return True

        board.area[x][y] = board.empty_cell
        return False

    def is_valid_move(self, x, y):
        return 0 <= x < len(self.board.area) and 0 <= y < len(self.board.area) and self.board.area[x][y] is self.board.empty_cell



