class Palindrome:
    @staticmethod
    def is_palindrome(s: str) -> bool:
        # Remove all non-alphanumeric characters and convert to lowercase
        s = ''.join(c for c in s if c.isalnum()).lower()
        # Check if the string reads the same forwards and backwards
        return s == s[::-1]
