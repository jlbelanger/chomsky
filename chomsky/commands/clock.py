from datetime import datetime
from chomsky.command import Command
from chomsky.number_to_text import NumberToText

class Clock(Command):
    id = 'clock'
    commands = None

    def run(self):
        now = datetime.now()
        hour = now.strftime('%-I')
        minute = now.strftime('%M')
        print('The time is now ' + NumberToText.convert(hour) + ' ' + NumberToText.convert(minute))
