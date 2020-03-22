from chomsky.audio import Audio
from chomsky.command import Command

class Wakeup(Command):
    def run(self):
        print('Awaiting command')
        Audio.play('sounds/wakeup.wav')
