import unittest

# Use the imports below to test either your array-based stack
# or your link-based version
# from stack_array import Stack
from stack_linked import Stack

class TestLab2(unittest.TestCase):
    def test_simple(self):
        stack = Stack(5)
        stack.push(0)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(),1)
        self.assertEqual(stack.peek(),0)
    def test1(self):
        stack = Stack(0)
        self.assertTrue(stack.is_empty())
        self.assertTrue(stack.capacity < 1)
        self.assertEqual(stack.size(), 0)
        self.assertTrue(stack.is_full())
        with self.assertRaises(IndexError):
            stack.push(9)

    def test2(self):
        stack = Stack(5)
        stack.push(4)
        stack.push(3)
        stack.push(2)
        stack.push(1)
        stack.push(0)
        self.assertTrue(stack.is_full())
        self.assertFalse(stack.is_empty())
        self.assertEqual(stack.size(), 5)
        with self.assertRaises(IndexError):
            stack.push(9)
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        self.assertTrue(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(), 0)
        with self.assertRaises(IndexError):
            stack.pop()
        with self.assertRaises(IndexError):
            stack.peek()

if __name__ == '__main__': 
    unittest.main()
