from Board import Board
from Knight import Knight
from sys import setrecursionlimit
from Args import Args

# ? NOTE:: Max board size is 44x44.


def main():
    args = Args()

    recursion_limit = args.handle_int_arg(args.depth, 15000)
    start_x = args.handle_int_arg(args.start_x, 0)
    start_y = args.handle_int_arg(args.start_y, 0)
    board_width = args.handle_int_arg(args.board_width, 8)
    board_height = args.handle_int_arg(args.board_height, 8)
    timeout = args.handle_int_arg(args.timeout, 50)

    setrecursionlimit(recursion_limit)
    knight = Knight(start_x, start_y)
    board = Board(board_width, board_height)
    board.set_knight(knight)

    # With default value (50 seconds)
    board.start(timeout)


if __name__ == "__main__":
    main()
