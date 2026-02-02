import unittest
from src.parenthesis import Parenthesis


class TestParenthesis(unittest.TestCase):

    def test_1(self):
        is_valid = Parenthesis.is_valid("()")
        self.assertTrue(is_valid)

    def test_2(self):
        is_valid = Parenthesis.is_valid("()[]{}")
        self.assertTrue(is_valid)

    def test_3(self):
        is_valid = Parenthesis.is_valid("(]")
        self.assertFalse(is_valid)

    def test_4(self):
        is_valid = Parenthesis.is_valid("([])")
        self.assertTrue(is_valid)

    def test_5(self):
        is_valid = Parenthesis.is_valid("([)]")
        self.assertFalse(is_valid)


if __name__ == '__main__':
    unittest.main()
