# Add, edit, or remove tests in this file.
# Treat it as your playground!

import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(program.balancedBrackets("()[]{}{"), False)

    def test_case_2(self):
        self.assertEqual(program.balancedBrackets("(((((({{{{{[[[[[([)])]]]]]}}}}}))))))"), False)

    def test_case_3(self):
        self.assertEqual(program.balancedBrackets("()()[{()})]"), False)

    def test_case_4(self):
        self.assertEqual(program.balancedBrackets("(()())((()()()))"), True)

    def test_case_5(self):
        self.assertEqual(program.balancedBrackets("{}()"), True)

    def test_case_6(self):
        self.assertEqual(program.balancedBrackets("()([])"), True)

    def test_case_7(self):
        self.assertEqual(program.balancedBrackets("((){{{{[]}}}})"), True)

    def test_case_8(self):
        self.assertEqual(program.balancedBrackets("([])(){}(())()()"), True)

    def test_case_9(self):
        self.assertEqual(program.balancedBrackets("((({})()))"), True)

    def test_case_10(self):
        self.assertEqual(program.balancedBrackets("(([]()()){})"), True)

    def test_case_11(self):
        self.assertEqual(
            program.balancedBrackets("(((((([[[[[[{{{{{{{{{{{{()}}}}}}}}}}}}]]]]]]))))))((([])({})[])[])[]([]){}(())"),
            True)

    def test_case_12(self):
        self.assertEqual(program.balancedBrackets("{[[[[({(}))]]]]}"), False)

    def test_case_13(self):
        self.assertEqual(program.balancedBrackets("[((([])([]){}){}){}([])[]((())"), False)

    def test_case_14(self):
        self.assertEqual(program.balancedBrackets(")[]}"), False)


if __name__ == "__main__":
    unittest.main()

