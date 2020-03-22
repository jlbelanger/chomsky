from chomsky.command import Command

class Cancel(Command):
    def run(self):
        print('Red alert cancelled.')
