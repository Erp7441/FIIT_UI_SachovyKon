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
        self.board.area[self.x][self.y] = self.representation

    def get_unvisited_neighbor_cells(self, x, y):
        # Number of unvisited neighbors
        num = 0

        # For each possible move
        for move_x, move_y in self.moves:

            # Get new position after the move is executed
            new_pos_x, new_pos_y = x + move_x, y + move_y

            if self.is_valid_move(new_pos_x, new_pos_y):
                # Increment number of unvisited neighbors
                num += 1

        return num

    def get_neighbor_cells(self, x, y):
        # Neighbor cells were we can move (also contains the neighbor's neighbor count)
        cells = []

        # For each possible move
        for move_x, move_y in self.moves:

            # Get new position after the move is executed
            new_pos_x, new_pos_y = x + move_x, y + move_y

            if self.is_valid_move(new_pos_x, new_pos_y):
                # Get the neighbors from the new position (current neighbor neighbors)
                num_neighbor_cells = self.get_unvisited_neighbor_cells(new_pos_x, new_pos_y)
                cells.append((new_pos_x, new_pos_y, num_neighbor_cells))

        # Sort cells where we can move (neighbors) by their neighbor count (ascending)
        cells.sort(key=lambda move: move[2])
        return cells

    def start(self):
        self.step_counter += 1

        # Starting the knight traversal
        if Knight.find_path(self.x, self.y, self.board, self.step_counter, self):
            return True

    def is_valid_move(self, x, y):
        # If not outside of bounds of the board
        return (0 <= x < len(self.board.area) and 0 <= y < len(self.board.area) and
                self.board.area[x][y] is self.board.empty_cell)

    @staticmethod
    def find_path(x, y, board, step_counter, figure):
        board.area[x][y] = "\t" + str(step_counter)

        # All the cells are marked
        if step_counter == len(board.area) ** 2:
            return True

        # Get list of neighbors sorted by the least amount of unvisited neighbor cells (Warnsdorffs Heuristic)
        neighbor_cells = figure.get_neighbor_cells(x, y)

        # For each neighbor
        for new_pos_x, new_pos_y, _ in neighbor_cells:
            # Try to find path from neighbor the neighbors position
            if Knight.find_path(new_pos_x, new_pos_y, board, step_counter+1, figure):
                return True

        # Reached a dead end. Moving backwards.
        board.area[x][y] = board.empty_cell
        return False
