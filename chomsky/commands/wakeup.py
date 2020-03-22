from chomsky.audio import Audio
from chomsky.command import Command
from .alert import Alert
from .clock import Clock
from .dinner import Dinner
from .weather import Weather

class Wakeup(Command):
    id = 'wakeup'
    commands = [Alert(), Dinner(), Clock(), Weather()]

    def run(self):
        Audio.play('sounds/wakeup.wav')
        print('Awaiting command')
