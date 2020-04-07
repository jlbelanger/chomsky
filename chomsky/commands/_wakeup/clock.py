from datetime import datetime
from chomsky.command import Command
from chomsky.number_to_text import NumberToText
from chomsky.audio import Audio

class Clock(Command):
    def run(self):
        now = datetime.now()
        hour = now.strftime('%-I')
        minute = now.strftime('%M')
        h = NumberToText.convert(hour)
        m = NumberToText.convert(minute)
        print('The time is ' + h + ' ' + m)

        filenames = [h] + m.split(' ')
        Audio.play('sounds/clock.wav')
        for filename in filenames:
            Audio.play('sounds/clock/' + filename + '.wav')
