import itertools
import unittest
from solver import generate_symbols, is_potential_match, get_potential_matches


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

    def test_guess_and_potential_match_all_wrong(self):
        is_p_m = is_potential_match(correct_positions=0, correct_symbols=0, guess="abcd", potential_match="abcd")
        self.assertFalse(is_p_m)

    def test_guess_and_potential_match_all_right(self):
        is_p_m = is_potential_match(correct_positions=4, correct_symbols=0, guess="abcd", potential_match="abcd")
        self.assertTrue(is_p_m)

    def test_guess_and_potential_match_symbols_correct(self):
        is_p_m = is_potential_match(correct_positions=0, correct_symbols=4, guess="abcd", potential_match="abcd")
        self.assertFalse(is_p_m)

    def test_not_potential_match(self):
        is_p_m_1 = is_potential_match(correct_positions=1, correct_symbols=3, guess="aaaa", potential_match="abcd")
        self.assertFalse(is_p_m_1)

    def test_potential_match(self):
        is_p_m = is_potential_match(correct_positions=1, correct_symbols=0, guess="abcd", potential_match="aaaa")
        self.assertTrue(is_p_m)

    def test_potential_matches_with_only_one_possible_match(self):
        valid_symbols = {'a', 'b', 'c'}
        combinations = [p for p in itertools.product(valid_symbols, repeat=3)]
        matches = get_potential_matches(3, 0, "abc", combinations)
        self.assertEqual([('a', 'b', 'c')], matches)

    def test_potential_matches_impossible_case_1(self):
        valid_symbols = {'a', 'b', 'c'}
        combinations = [p for p in itertools.product(valid_symbols, repeat=3)]
        matches = get_potential_matches(0, 1, "aaa", combinations)
        self.assertEqual([], matches)

    def test_potential_matches_impossible_case_2(self):
        valid_symbols = {'a', 'b', 'c'}
        combinations = [p for p in itertools.product(valid_symbols, repeat=3)]
        matches = get_potential_matches(0, 0, "abc", combinations)
        self.assertEqual([], matches)

    def test_potential_matches_one_possible_match(self):
        valid_symbols = {'a', 'b', 'c'}
        combinations = [p for p in itertools.product(valid_symbols, repeat=3)]
        matches = get_potential_matches(3, 0, "abc", combinations)
        self.assertEqual([('a', 'b', 'c')], matches)

    def test_potential_matches_two_possible_match(self):
        valid_symbols = {'a', 'b', 'c'}
        combinations = [p for p in itertools.product(valid_symbols, repeat=3)]
        combinations.sort()
        matches = get_potential_matches(0, 3, "abc", combinations)
        self.assertEqual([('b', 'c', 'a'), ('c', 'a', 'b')], matches)

    def test_potential_matches_three_possible_match(self):
        valid_symbols = {'a', 'b', 'c'}
        combinations = [p for p in itertools.product(valid_symbols, repeat=3)]
        combinations.sort()
        matches = get_potential_matches(1, 0, "abc", combinations)
        self.assertEqual([('a', 'a', 'a'), ('b', 'b', 'b'), ('c', 'c', 'c')], matches)


if __name__ == '__main__':
    unittest.main()
