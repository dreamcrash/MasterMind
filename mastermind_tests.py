import unittest
from solver import generate_symbols


class MasterMindTestCase(unittest.TestCase):
    def test_zero_symbols(self):
        symbols = generate_symbols(0)
        self.assertEqual([], symbols)

    def test_minimal_symbols(self):
        symbols = generate_symbols(3)
        self.assertEqual(['a', 'b', 'c'], symbols)

    def test_max_symbols(self):
        symbols = generate_symbols(8)
        self.assertEqual(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], symbols)


if __name__ == '__main__':
    unittest.main()
