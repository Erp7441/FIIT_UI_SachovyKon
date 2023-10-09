from sys import setrecursionlimit

from Args import Args
from Board import Board
from Knight import Knight
from random import choices


def main():
    args = Args()

    recursion_limit = args.parse_int(args.depth, 10 ** 6)
    setrecursionlimit(recursion_limit)

    try:
        from resource import setrlimit, RLIMIT_STACK
        setrlimit(RLIMIT_STACK, (recursion_limit * 537, -1))
    except ModuleNotFoundError:
        pass

    board_width = args.parse_int(args.board_width, 8)
    board_height = args.parse_int(args.board_height, 8)
    timeout = args.parse_int(args.timeout, 50)

    if args.random_start is False:
        start_x = [args.parse_int(args.start_x, 0)]
        start_y = [args.parse_int(args.start_y, 0)]
    else:
        start_x = choices(range(0, board_width), k=10)
        start_y = choices(range(0, board_height), k=10)

    for i, _ in enumerate(start_x):
        knight = Knight(start_x[i], start_y[i])
        board = Board(board_width, board_height)
        board.set_knight(knight)

        # With default value (50 seconds)
        if board.start(timeout) is True:
            return


if __name__ == "__main__":
    main()
