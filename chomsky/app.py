from chomsky.commands.wakeup import Wakeup
from chomsky.commands.quit import Quit
from chomsky.audio import Audio
from chomsky.listener import Listener
from chomsky.matcher import Matcher

class App():
    def __init__(self):
        self.default_commands = [Wakeup()]
        self.available_commands = [Wakeup()]

    def start(self):
        while True:
            self.run()

    def run(self):
        # Print the list of available commands. (Quit is always available.)
        q = Quit()
        command_list = ','.join(map(lambda x: x.pattern(), [q] + self.available_commands))
        print("\nAvailable commands: " + str(command_list))

        # Wait for user input.
        a = Listener.listen()

        # Test for quit command.
        if Matcher.match(a, q.pattern()):
            q.run()
            return

        # Test for all other available commands.
        command_found = False
        for command in self.available_commands:
            if Matcher.match(a, command.pattern()):
                command_found = True
                command.run()

                # Load new commands.
                self.available_commands = command.available_commands()
                if self.available_commands is None:
                    self.available_commands = self.default_commands

                break

        if not command_found:
            Audio.play('sounds/error.wav')
            print('Command not found')
