from .command import Command

class Song(Command):
    id = 's'
    commands = None

    def run(self):
        print('La la-la la-la, la-la la la-la la-la, la la-la la-la la. La la-la la-la, la la-la la-la, la la-la la la-la!')
