import sys
from chomsky.command import Command

class Quit(Command):
    def run(self):
        sys.exit()
