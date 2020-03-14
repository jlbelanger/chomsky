class NumberToText():
    @staticmethod
    def convert(number):
        numbers = {
            '1': 'one',
            '2': 'two',
            '3': 'three',
            '4': 'four',
            '5': 'five',
            '6': 'six',
            '7': 'seven',
            '8': 'eight',
            '9': 'nine',
            '10': 'ten',
            '11': 'eleven',
            '12': 'twelve',
            '13': 'thirteen',
            '14': 'fourteen',
            '15': 'fifteen',
            '16': 'sixteen',
            '17': 'seventeen',
            '18': 'eighteen',
            '19': 'nineteen',
            '20': 'twenty',
            '30': 'thirty',
            '40': 'forty',
            '50': 'fifty',
            '60': 'sixty',
            '70': 'seventy',
            '80': 'eighty',
            '90': 'ninety',
            '100': 'one hundred',
        }

        number = str(number)

        if number in numbers:
            return numbers[number]

        parts = list(number)
        output = []
        i = 0

        if parts[0] == '-':
            output.append('minus')
            parts.pop(0)

        while parts[0] == '0':
            output.append('oh')
            parts.pop(0)

        num_parts = len(parts)

        for part in parts:
            part = part.ljust(num_parts - i, '0')
            if part in numbers:
                output.append(numbers[part])
            i += 1

        return ' '.join(output)
