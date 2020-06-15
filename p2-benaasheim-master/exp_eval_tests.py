# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):
    def test_postfix_eval_01(self):
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)

    def test_postfix_eval_02(self):
        try:
            postfix_eval("blah")
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_03(self):
        try:
            postfix_eval("4 +")
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_04(self):
        try:
            postfix_eval("1 2 3 +")
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")
    
    def test_postfix_eval_05(self):
        try:
            postfix_eval("8 6 - blah")
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")
    
    def test_postfix_eval_06(self):
        try:
            postfix_eval("5 f +")
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")
    
    def test_postfix_eval_07(self):
        try:
            postfix_eval("")
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_08(self):
        try:
            postfix_eval("8 6 * blah")
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_09(self):
        try:
            postfix_eval("8 6 ** blah")
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_10(self):
        try:
            postfix_eval("8 6 / blah")
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_11(self):
        try:
            postfix_eval("8 6 >> blah")
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")
    
    def test_postfix_eval_12(self):
        try:
            postfix_eval("8 6 << blah")
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")
    
    def test_postfix_eval_13(self):
        try:
            postfix_eval("8 0 / 9")
        except ValueError as e:
            self.assertEqual(str(e), "")
    
    def test_postfix_eval_14(self):
        try:
            postfix_eval("4 5 + +")
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")
    
    def test_postfix_eval_15(self):
        try:
            postfix_eval("8 6.5 >>")
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")
    
    def test_postfix_eval_16(self):
        try:
            postfix_eval("8 6.5 <<")
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")
    
    def test_infix_to_postfix_01(self):
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(infix_to_postfix("6"), "6")
        self.assertEqual(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 ) ** 2 ** 3"), "3 4 2 * 1 5 - 2 3 ** ** / +")
    def test_prefix_to_postfix(self):
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")

if __name__ == "__main__":
    unittest.main()
