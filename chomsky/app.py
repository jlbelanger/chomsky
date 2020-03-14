from chomsky.commands.wakeup import Wakeup
from chomsky.commands.quit import Quit
from chomsky.audio import Audio

class App():
    def __init__(self):
        self.default_commands = [Wakeup()]
        self.available_commands = [Wakeup()]

    def start(self):
        while True:
            self.listen()

    def listen(self):
        q = Quit()
        command_list = ','.join(map(lambda x: x.pattern(), [q] + self.available_commands))
        print("\nAvailable commands: " + str(command_list))

        a = input('> ')

        if App.match(a, q.pattern()):
            q.run()
        else:
            command_found = False

            for command in self.available_commands:
                if App.match(a, command.pattern()):
                    command_found = True
                    command.run()
                    self.available_commands = command.available_commands()
                    if self.available_commands is None:
                        self.available_commands = self.default_commands
                    break

            if not command_found:
                Audio.play('sounds/error.wav')
                print('Command not found')

    @staticmethod
    def match(a, b):
        return a == b
