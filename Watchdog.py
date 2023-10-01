import os
import signal
import threading


class Watchdog:
    def __init__(self, timeout):
        self.timeout = timeout
        self.timer = threading.Timer(self.timeout, Watchdog.timed_out)

    @staticmethod
    def timed_out():
        print("Execution timed out!")
        pid = os.getpid()
        os.kill(pid, signal.SIGTERM)

    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.cancel()
