from random import choice
import config
from chomsky.audio import Audio
from chomsky.command import Command

class Dinner(Command):
    def run(self):
        print(choice(config.DINNER_OPTIONS))
        Audio.play('sounds/dinner.wav')
