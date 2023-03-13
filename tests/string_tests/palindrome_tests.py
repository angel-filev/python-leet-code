import unittest

from strings.palindrome import Palindrome

class TestPalindrome(unittest.TestCase):
    def test_palindrome_true(self):
        s = "A man, a plan, a canal: Panama"
        self.assertTrue(Palindrome.is_palindrome(s))

    def test_palindrome_false(self):
        s = "race a car"
        self.assertFalse(Palindrome.is_palindrome(s))

    def test_palindrome_empty_string(self):
        s = " "
        self.assertTrue(Palindrome.is_palindrome(s))


if __name__ == '__main__':
    unittest.main()
