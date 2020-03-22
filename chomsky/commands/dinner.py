from random import choice
import config
from chomsky.audio import Audio
from chomsky.command import Command

class Dinner(Command):
    id = 'dinner'
    commands = None

    def run(self):
        Audio.play('sounds/dinner.wav')
        print(choice(config.DINNER_OPTIONS))
