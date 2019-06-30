# Add, edit, or remove tests in this file.
# Treat it as your playground!

import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(program.isPalindrome("a"), True)

    def test_case_2(self):
        self.assertEqual(program.isPalindrome("ab"), False)

    def test_case_3(self):
        self.assertEqual(program.isPalindrome("aba"), True)

    def test_case_4(self):
        self.assertEqual(program.isPalindrome("abb"), False)

    def test_case_5(self):
        self.assertEqual(program.isPalindrome("abba"), True)

    def test_case_6(self):
        self.assertEqual(program.isPalindrome("abcdcba"), True)

    def test_case_7(self):
        self.assertEqual(program.isPalindrome("abcdefghhgfedcba"), True)

    def test_case_8(self):
        self.assertEqual(program.isPalindrome("abcdefghihgfedcba"), True)

    def test_case_9(self):
        self.assertEqual(program.isPalindrome("abcdefghihgfeddcba"), False)


if __name__ == "__main__":
    unittest.main()

