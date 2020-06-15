import unittest
from tsort import *

class TestTsort(unittest.TestCase):

    def test_f1(self):
        input = ['101', '102', '102', '103', '103', '315', '225', '315', '103', '357', '315', '357', '141', '102', '102', '225']
        expect = [['101', 0, ['102']], ['102', 0, ['103', '225']], ['103', 0, ['315', '357']], ['225', 0, ['315']], ['315', 0, ['357']], ['141', 0, ['102']], ['357', 0, []]]
        actual = f1(input)
        self.assertEqual(actual, expect)

    def test_f2(self):
        input = [['101', 0, ['102']], ['102', 0, ['103', '225']], ['103', 0, ['315', '357']], ['225', 0, ['315']], ['315', 0, ['357']], ['141', 0, ['102']]]
        expect = [['101', 0, ['102']], ['102', 2, ['103', '225']], ['103', 1, ['315', '357']], ['225', 1, ['315']], ['315', 2, ['357']], ['141', 0, ['102']]]
        f2(input)
        self.assertEqual(input, expect)

    def test_f3(self):
        input = [['101', 0, ['102']], ['102', 2, ['103', '225']], ['103', 1, ['315', '357']], ['225', 1, ['315']], ['315', 2, ['357']], ['141', 0, ['102']]]
        ss = Stack(len(input))
        expect = [['101', 0, ['102']], ['102', 2, ['103', '225']], ['103', 1, ['315', '357']], ['225', 1, ['315']], ['315', 2, ['357']], ['141', 0, ['102']]]
        f3(input, ss)
        self.assertEqual(input, expect)
        itr = [['101', 0, ['102']], ['141', 0, ['102']]]
        self.assertEqual(ss.items[:len(itr)], itr)

    def test_f4(self):
        input = ['101', '102', '102', '103', '103', '315', '225', '315', '103', '357', '315', '357', '141', '102', '102', '225']
        expect = [['101', 0, ['102']], ['102', 0, ['103', '225']], ['103', 0, ['315', '357']], ['225', 0, ['315']], ['315', 0, ['357']], ['141', 0, ['102']], ['357', 0, []]]
        actual = f1(input)
        self.assertEqual(actual, expect)
        ss = Stack(len(actual))
        f2(actual)
        f3(actual, ss)
        rlis = f4(actual, ss, input)
        fff = "141\n101\n102\n225\n103\n315\n357"
        self.assertEqual(fff.split("\n"), rlis)

    def test_01(self):
        input = ['101', '102', '102', '103', '103', '315', '225', '315', '103', '357', '315', '357', '141', '102', '102', '225']
        expect = "141\n101\n102\n225\n103\n315\n357"
        actual = tsort(input)
        self.assertEqual(actual.strip(), expect)

    def test_011(self):
        input = ['141', '102', '102', '103', '103', '315', '225', '315', '103', '357', '315', '357', '101', '102', '102', '225']
        expect = "101\n141\n102\n225\n103\n315\n357"
        actual = tsort(input)
        self.assertEqual(actual.strip(), expect)

    def test_02(self):
        input = ['blue', 'black', 'red', 'blue', 'red', 'green', 'green', 'blue', 'green', 'purple', 'purple', 'blue']
        expect = "red\ngreen\npurple\nblue\nblack"
        actual = tsort(input)
        self.assertEqual(actual.strip(), expect)

    def test_03(self):
        input = ['1', '2', '1', '9', '1', '8', '9', '8', '9', '10', '8', '11', '10', '11', '2', '3', '3', '11', '3', '4', '4', '7', '4', '5', '7', '5', '7', '13', '7', '6', '6', '14', '6', '12']
        expect = "1\n9\n10\n8\n2\n3\n4\n7\n6\n12\n14\n13\n5\n11"
        actual = tsort(input)
        self.assertEqual(actual.strip(), expect)

    def test_04(self):
        input = ['3', '8', '3', '10', '5', '11', '7', '8', '7', '11', '8', '9', '11', '2', '11', '9', '11', '10']
        expect = "7\n5\n11\n2\n3\n10\n8\n9"
        actual = tsort(input)
        self.assertEqual(actual.strip(), expect)

    def test_err1(self):
        with self.assertRaises(ValueError):
            f1(["a"])

    def test_err2(self):
        with self.assertRaises(ValueError):
            f1(["", "101"])

    def test_err3(self):
        with self.assertRaises(ValueError):
            f1(["101", ""])

    def test_err4(self):
        input = ["101", "102", "102", "101"]
        a = f1(input)
        a = sortr(a)
        f2(a)
        ss = Stack(len(a))
        with self.assertRaises(ValueError):
            f3(a, ss)

    def test_err5(self):
        input = ["100", "101", "101", "102", "102", "101"]
        a = f1(input)
        a = sortr(a)
        f2(a)
        ss = Stack(len(a))
        f3(a, ss)
        with self.assertRaises(ValueError):
            f4(a, ss, input)

    def test_err6(self):
        input = ["a", "b", "a", "c", "b", "d", "c", "e", "d", "c", "e", "f", "f", "d"]
        with self.assertRaises(ValueError):
            tsort(input)
        input = ['1', '2', '2', '3', '3', '4', '4', '1', '3', '5']
        with self.assertRaises(ValueError):
            tsort(input)

    def test_err7(self):
        input = ["100", "101", "101", "102", "102", "101"]
        with self.assertRaises(ValueError):
            tsort(input)

    def test_onesy(self):
        input = ["1", "1"]
        with self.assertRaises(ValueError):
            tsort(input)

    def test_10(self):
        input = []
        with self.assertRaises(ValueError):
            tsort(input)

    def test_09(self):
        input = ['blue', 'blue', 'blue', 'black', 'red', 'blue', 'red', 'green', 'green', 'blue', 'green', 'purple', 'purple', 'blue']
        with self.assertRaises(ValueError):
            print(tsort(input))

if __name__ == "__main__":
    unittest.main()
