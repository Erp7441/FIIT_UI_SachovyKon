from Board import Board
from Knight import Knight
from argparse import ArgumentParser


def main():
    knight = Knight(0, 0)
    board = Board(31, 31)
    board.set_knight(knight)

    # With timeout value from arguments
    args = get_args()
    if args.timeout is not None:
        try:
            board.start(int(args.timeout))
            return
        except ValueError:
            print("Could not convert timeout argument value \"{}\" to integer value!".format(args.timeout))
            if not get_confirmation():
                return
            print("Running with default value...\n")

    # With default value (50 seconds)
    board.start()


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
    return parser.parse_args()


if __name__ == "__main__":
    main()


# Notes:
# Knight can move in a "L" shape
