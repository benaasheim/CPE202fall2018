import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
    def test_max_list_iter1(self):
        self.assertEqual(max_list_iter([]),None)
    def test_max_list_iter2(self):
        self.assertEqual(max_list_iter([0,1,2,3,4,5,6,7,8,9]),9)
    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])

    def test_reverse_rec1(self):
        self.assertEqual(reverse_rec([90,2,3]),[3,2,90])

    def test_reverse_rec2(self):
        self.assertEqual(reverse_rec([1]),[1])
    
    def test_reverse_rec3(self):
        int_list = None
        with self.assertRaises(ValueError):
            reverse_rec(int_list)
    
    def test_bin_search(self):
        with self.assertRaises(ValueError):
            bin_search(0, 0, 0, None)
    
    def test_bin_search1(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = 8
        self.assertEqual(bin_search(4, low, high, list_val),4)
    
    def test_bin_search2(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = 8
        self.assertEqual(bin_search(0, low, high, list_val),0)
    def test_bin_search3(self):
        list_val =[]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(0, 0, 4, list_val),None)
    def test_bin_search4(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = 9
        self.assertEqual(bin_search(7, low, high, list_val),5)
    
if __name__ == "__main__":
        unittest.main()
