from chomsky.audio import Audio
from chomsky.command import Command

class Rude(Command):
    def run(self):
        Audio.play('sounds/rude.wav')
