import sys
from .command import Command

class Quit(Command):
    id = 'q'
    commands = None

    def run(self):
        sys.exit()
