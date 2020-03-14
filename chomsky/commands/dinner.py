from random import choice
import config
from .command import Command

class Dinner(Command):
    id = 'd'
    commands = None

    def run(self):
        print(choice(config.DINNER_OPTIONS))
