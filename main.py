from Board import Board
from Knight import Knight
from argparse import ArgumentParser
from sys import setrecursionlimit

# ? NOTE:: Max board size is 44x44.


def main():
    args = get_args()

    recursion_limit = handle_int_arg(args.depth, 15000)
    start_x = handle_int_arg(args.start_x, 0)
    start_y = handle_int_arg(args.start_y, 0)
    board_width = handle_int_arg(args.board_width, 8)
    board_height = handle_int_arg(args.board_height, 8)
    timeout = handle_int_arg(args.timeout, 50)

    setrecursionlimit(recursion_limit)
    knight = Knight(start_x, start_y)
    board = Board(board_width, board_height)
    board.set_knight(knight)

    # With default value (50 seconds)
    board.start(timeout)


def get_confirmation():
    response = ''
    while response != 'Y' and response != 'N':
        print("Do you wish to continue? (y/n): ", end='')
        response = input().upper()
    return response == 'Y'


def get_args():
    # Parsing arguments
    parser = ArgumentParser(description="Euler's Horse by Martin Szabo")
    parser.add_argument("-t", "--timeout", dest="timeout", help="How long should the program wait before timing out")
    parser.add_argument("-d", "--depth", dest="depth", help="Maximum recursion depth. Increase this with large "
                                                            "chessboard proportions")
    parser.add_argument("-W", "--width", dest="board_width", help="Chessboard width")
    parser.add_argument("-H", "--height", dest="board_height", help="Chessboard height")
    parser.add_argument("-X", "--start-x", dest="start_x", help="Starting X coordinate")
    parser.add_argument("-Y", "--start-y", dest="start_y", help="Starting Y coordinate")
    return parser.parse_args()


def handle_int_arg(arg, default_value):
    value = convert_arg_to_int(arg)
    value = value if value is not None else default_value
    return value


def convert_arg_to_int(arg):
    if arg is not None:
        try:
            return int(arg)
        except ValueError:
            print("Could not convert argument value \"{}\" to integer value!".format(arg))
            if not get_confirmation():
                exit(1)
            return None


if __name__ == "__main__":
    main()
