class Command:
    id = ''
    commands = []

    def pattern(self):
        return self.id

    def available_commands(self):
        return self.commands

    def run(self):
        raise NotImplementedError('Run method not implemented')
