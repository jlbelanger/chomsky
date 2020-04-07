import sys
from chomsky.audio import Audio
from chomsky.command import Command

class Quit(Command):
    def run(self):
        Audio.play('sounds/quit.wav')
        sys.exit()
