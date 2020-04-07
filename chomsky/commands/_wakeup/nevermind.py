from chomsky.audio import Audio
from chomsky.command import Command

class Nevermind(Command):
    def run(self):
        Audio.play('sounds/nevermind.wav')
        print('OK')
