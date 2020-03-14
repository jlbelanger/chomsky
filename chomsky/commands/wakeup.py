from chomsky.audio import Audio
from .clock import Clock
from .command import Command
from .dinner import Dinner
from .song import Song
from .weather import Weather

class Wakeup(Command):
    id = 'w'
    commands = [Dinner(), Song(), Clock(), Weather()]

    def run(self):
        Audio.play('sounds/listening.wav')
        print('Awaiting command')
