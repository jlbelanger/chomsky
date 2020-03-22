from chomsky.audio import Audio
from chomsky.command import Command

class Alert(Command):
    id = 'alert'
    commands = None

    def run(self):
        Audio.play('sounds/alert.wav')
