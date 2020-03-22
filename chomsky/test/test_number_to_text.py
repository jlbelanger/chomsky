import unittest
from chomsky.number_to_text import NumberToText

class TestNumberToText(unittest.TestCase):
    def test_convert(self):
        self.assertEqual(NumberToText.convert('-147'), 'minus one hundred forty seven')
        self.assertEqual(NumberToText.convert('-47'), 'minus forty seven')
        self.assertEqual(NumberToText.convert('-40'), 'minus forty')
        self.assertEqual(NumberToText.convert('-1'), 'minus one')
        self.assertEqual(NumberToText.convert('1'), 'one')
        self.assertEqual(NumberToText.convert('2'), 'two')
        self.assertEqual(NumberToText.convert('10'), 'ten')
        self.assertEqual(NumberToText.convert('07'), 'oh seven')
        self.assertEqual(NumberToText.convert('007'), 'oh oh seven')
        self.assertEqual(NumberToText.convert('40'), 'forty')
        self.assertEqual(NumberToText.convert('47'), 'forty seven')
        self.assertEqual(NumberToText.convert('140'), 'one hundred forty')
        self.assertEqual(NumberToText.convert('147'), 'one hundred forty seven')

if __name__ == '__main__':
    unittest.main()
