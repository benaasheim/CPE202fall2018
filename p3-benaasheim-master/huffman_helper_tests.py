
import unittest
import filecmp
import subprocess
from huffman import *

class TestList(unittest.TestCase):
    def test_cnt_freq2(self):
        freqlist    = parse_header("97 2 98 4 99 8 100 16 102 2")
        anslist = [2, 4, 8, 16, 0, 2, 0] 
        self.assertListEqual(freqlist[97:104], anslist)

    def test_11_textfile(self):
        huffman_decode("file1_soln.txt", "out1.txt")
        err = subprocess.call("diff -wb out1.txt file1.txt", shell = True)
        self.assertEqual(err, 0)

    def test_22_textfile(self):
        huffman_decode("file2_soln.txt", "out2.txt")
        err = subprocess.call("diff -wb out2.txt file2.txt", shell = True)
        self.assertEqual(err, 0)

    def test33_textfile(self):
        try:
            huffman_decode("file5890.txt", "out1.txt")
        except FileNotFoundError as e:
            self.assertEqual(str(e), "FileNotFoundError")
        
if __name__ == '__main__': 
    unittest.main()
