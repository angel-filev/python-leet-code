# Unit tests
import unittest

from src.strings.balanced_parentheses import BalancedParentheses


class BalancedParenthesesTests(unittest.TestCase):
    def test_example_1(self):
        self.assertTrue(BalancedParentheses.is_balanced("()"))

    def test_example_2(self):
        self.assertTrue(BalancedParentheses.is_balanced("()[]{}"))

    def test_example_3(self):
        self.assertFalse(BalancedParentheses.is_balanced("(]"))

    def test_empty_string(self):
        self.assertTrue(BalancedParentheses.is_balanced(""))

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            BalancedParentheses.is_balanced("()" * 104)

if __name__ == "__main__":
    unittest.main()
