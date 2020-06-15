import unittest
import filecmp
import subprocess
from huffman import *

class TestList(unittest.TestCase):
    def test_rpr(self):
        a = HuffmanNode(97, 3)
        self.assertEqual(a.__repr__(), "97|3")

    def test__NLR(self):
        a = HuffmanNode(97, 2)
        b = HuffmanNode(98, 3)
        c = HuffmanNode(197, 1)
        d = HuffmanNode(198, 1)
        cc = combine(c, d)
        aa = combine(a, cc)
        bb = combine(b, aa)
        q = []
        bb.NLR(q, "")
        qq = [(98, "0"), (97, "10"), (197, "110"), (198, "111")]
        self.assertEqual(q, qq)

    def test_comes_before(self):
        a = HuffmanNode(97, 2)
        b = HuffmanNode(98, 2)
        self.assertTrue(comes_before(a, b))
        self.assertFalse(comes_before(b, a))
        a = HuffmanNode(98, 1)
        b = HuffmanNode(98, 2)
        self.assertTrue(comes_before(a, b))
        self.assertFalse(comes_before(b, a))

    def test_cnt_freq(self):
        freqlist = cnt_freq("file2.txt")
        anslist = [2, 4, 8, 16, 0, 2, 0]
        self.assertListEqual(freqlist[97:104], anslist)

    def test_create_huff_tree(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        self.assertEqual(hufftree.freq, 32)
        self.assertEqual(hufftree.char, 97)
        left = hufftree.left
        self.assertEqual(left.freq, 16)
        self.assertEqual(left.char, 97)
        right = hufftree.right
        self.assertEqual(right.freq, 16)
        self.assertEqual(right.char, 100)

    def test_HuffmanSort(self):
        a = HuffmanNode(97, 2)
        b = HuffmanNode(98, 3)
        c = HuffmanNode(197, 1)
        d = HuffmanNode(198, 1)
        cc = combine(c, d)
        aa = combine(a, cc)
        bb = combine(b, aa)
        q = []
        bb.NLR(q, "")
        qqq = [(98, "0"), (97, "10"), (197, "110"), (198, "111")]
        self.assertEqual(q, qqq)

    def test_create_code(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('d')], '1')
        self.assertEqual(codes[ord('a')], '0000')
        self.assertEqual(codes[ord('f')], '0001')

    def test_make_code(self):
        a = [None]*97
        b = [None]*18
        c = [None]*138
        qqq = a + ["10","0"] + b + ["110","111"] + c
        self.assertEqual(make_code(qqq, "file0.txt"), "0001010110111")

    def test_create_header(self):
        freqlist = cnt_freq("file2.txt")
        self.assertEqual(create_header(freqlist), "97 2 98 4 99 8 100 16 102 2")

    def test_01_textfile(self):
        huffman_encode("file1.txt", "file1_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb file1_out.txt file1_soln.txt", shell = True)
        self.assertEqual(err, 0)

    def test_02_textfile(self):
        huffman_encode("file2.txt", "file2_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb file2_out.txt file2_soln.txt", shell = True)
        self.assertEqual(err, 0)

    def test_03_textfile(self):
        huffman_encode("multiline.txt", "multiline_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb multiline_out.txt multiline_soln.txt", shell = True)
        self.assertEqual(err, 0)

    def test_04_textfile(self):
        huffman_encode("declaration.txt", "declaration_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb declaration_out.txt declaration_soln.txt", shell = True)
        self.assertEqual(err, 0)

    def test_19_textfile(self):
        huffman_encode("wnp.txt", "warout.txt")
        huffman_decode("warout.txt", "wnp_new.txt")
        err = subprocess.call("diff -wb wnp.txt wnp_new.txt", shell = True)
        self.assertEqual(err, 0)

    def test_cnt_freq2(self):
        freqlist = parse_header("97 2 98 4 99 8 100 16 102 2")
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

    def testy_empty(self):
        huffman_decode("empty.txt", "empty_out.txt")
        err = subprocess.call("diff -wb empty_out.txt empty_soln.txt", shell = True)
        self.assertEqual(err, 0)

    def test_shorty(self):
        huffman_encode("shorty.txt", "shorty_out.txt")
        err = subprocess.call("diff -wb shorty_out.txt shorty_soln.txt", shell = True)
        self.assertEqual(err, 0)

    def test_shorty_de(self):
        huffman_decode("shorty_soln.txt", "shorty_out.txt")
        err = subprocess.call("diff -wb shorty.txt shorty_out.txt", shell = True)
        self.assertEqual(err, 0)

if __name__ == '__main__':
    unittest.main()
