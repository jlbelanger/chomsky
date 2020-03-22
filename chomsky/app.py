import glob
import sys
from chomsky.audio import Audio
from chomsky.listener import Listener
from chomsky.trainer import Trainer

class App():
    def __init__(self):
        self.path = []
        self.available_commands = ['quit', 'wakeup']

    def start(self):
        if Trainer.should_train():
            Trainer.train()

        self.print_commands()

        while True:
            self.loop()

    def loop(self):
        # Wait for user input.
        word = Listener().listen()

        # Test for all available commands.
        for command in self.available_commands:
            if word == command.split('/')[-1]:
                self.run_command(command)
                self.load_commands(command)
                self.print_commands()
                return

        # If there is a path, then we are awake. We only want to play an error message if we are awake.
        if self.path:
            print('Command not found')
            Audio.play('sounds/error.wav')
        else:
            print('...')

    def run_command(self, command):
        command = ('chomsky/commands/' + command).replace('/', '.')
        class_name = command.split('.')[-1].capitalize()
        __import__(command)
        f = sys.modules[command]
        some_class = getattr(f, class_name)
        command = some_class()
        command.run()

    def load_commands(self, command):
        self.path.append('_' + command)
        available_commands = glob.glob('chomsky/commands/' + '/'.join(self.path) + '/*')
        available_commands = list(map(lambda x: x.replace('chomsky/commands/', '').replace('.py', ''), available_commands))
        available_commands = filter(lambda x: x.split('/')[-1][0] != '_', available_commands)
        available_commands = sorted(available_commands)

        if not available_commands:
            self.path = []
            self.available_commands = ['quit', 'wakeup']
        else:
            self.available_commands = ['quit'] + available_commands

    def print_commands(self):
        c = list(map(lambda x: x.split('/')[-1], self.available_commands))
        print("\nAvailable commands: " + ', '.join(c))
