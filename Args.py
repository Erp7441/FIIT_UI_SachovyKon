import os
import signal
from argparse import ArgumentParser


class Args:

    def __init__(self):
        # Parsing arguments
        self.parser = ArgumentParser(description="Euler's Horse by Martin Szabo")
        self.parser.add_argument("-t", "--timeout", dest="timeout", help="How long should the program wait before time out")
        self.parser.add_argument("-d", "--depth", dest="depth", help="Maximum recursion depth. Increase this with large "
                                                                "chessboard proportions")
        self.parser.add_argument("-W", "--width", dest="board_width", help="Chessboard width")
        self.parser.add_argument("-H", "--height", dest="board_height", help="Chessboard height")
        self.parser.add_argument("-X", "--start-x", dest="start_x", help="Starting X coordinate")
        self.parser.add_argument("-Y", "--start-y", dest="start_y", help="Starting Y coordinate")

        args_dict = self.parser.parse_args().__dict__

        for k, v in args_dict.items():
            setattr(self, k, v)

    def parse_int(self, arg, default_value):
        value = self.__convert_arg_to_int(arg)
        value = value if value is not None else default_value
        return value

    def __convert_arg_to_int(self, arg):
        if arg is not None:
            try:
                return int(arg)
            except ValueError:
                print("Could not convert argument value \"{}\" to integer value!".format(arg))
                if not self.__get_confirmation():
                    pid = os.getpid()
                    os.kill(pid, signal.SIGTERM)
                print("Using default value...\n")
                return None

    @staticmethod
    def __get_confirmation():
        response = ''
        while response != 'Y' and response != 'N':
            print("Do you wish to continue? (y/n): ", end='')
            response = input().upper()
        return response == 'Y'
