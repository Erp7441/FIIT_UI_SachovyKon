from sys import setrecursionlimit

from Args import Args
from Board import Board
from Knight import Knight


# ? NOTE:: Max board size is 44x44.


def main():
    args = Args()

    recursion_limit = args.parse_int(args.depth, 15000)
    start_x = args.parse_int(args.start_x, 0)
    start_y = args.parse_int(args.start_y, 0)
    board_width = args.parse_int(args.board_width, 8)
    board_height = args.parse_int(args.board_height, 8)
    timeout = args.parse_int(args.timeout, 50)

    setrecursionlimit(recursion_limit)
    knight = Knight(start_x, start_y)
    board = Board(board_width, board_height)
    board.set_knight(knight)

    # With default value (50 seconds)
    board.start(timeout)


if __name__ == "__main__":
    main()
