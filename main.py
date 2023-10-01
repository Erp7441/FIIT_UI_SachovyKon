from Board import Board
from Knight import Knight

knight = Knight(0, 0)
board = Board(31, 31)
board.set_knight(knight)

board.start()

# Notes:
# Knight can move in a "L" shape
