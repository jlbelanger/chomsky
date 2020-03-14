from datetime import datetime
from .command import Command
from ..number_to_text import NumberToText

class Clock(Command):
    id = 't'
    commands = None

    def run(self):
        now = datetime.now()
        hour = now.strftime('%-I')
        minute = now.strftime('%M')
        print('The time is now ' + NumberToText.convert(hour) + ' ' + NumberToText.convert(minute))
