from chomsky.audio import Audio
from chomsky.command import Command

class Alert(Command):
    def run(self):
        print('RED ALERT')
        Audio.play('sounds/alert.wav')
