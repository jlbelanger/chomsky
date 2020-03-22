import sys
from chomsky.command import Command

class Quit(Command):
    id = 'quit'
    commands = None

    def run(self):
        sys.exit()
