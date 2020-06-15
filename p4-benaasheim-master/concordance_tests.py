import unittest
import filecmp
from concordance import *

class TestList(unittest.TestCase):

    def test_00(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        self.assertTrue(conc.stop_table.in_table("a"))
        conc.load_concordance_table("blank.txt")
        self.assertEqual(conc.concordance_table.get_value("a"), None)
        self.assertEqual(conc.concordance_table.get_index("a"), None)

    def test_01(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        self.assertTrue(conc.stop_table.in_table("to"))
        conc.load_concordance_table("file1.txt")
        self.assertEqual(conc.concordance_table.get_index("fourscore"), 43)
        conc.write_concordance("file1_con.txt")
        self.assertTrue(filecmp.cmp("file1_con.txt", "file1_sol.txt"))

    def test_02(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("file2.txt")
        conc.write_concordance("file2_con.txt")
        self.assertTrue(filecmp.cmp("file2_con.txt", "file2_sol.txt"))

    def test_03(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("declaration.txt")
        self.assertTrue(conc.stop_table.in_table("them"))
        self.assertEqual(conc.concordance_table.get_value("abiing"), None)
        self.assertEqual(conc.concordance_table.get_index("abiing"), None)
        conc.write_concordance("declaration_con.txt")
        self.assertTrue(filecmp.cmp("declaration_con.txt", "declaration_sol.txt"))

    def test_04(self):
        conc = Concordance()
        with self.assertRaises(FileNotFoundError):
            conc.load_stop_table("stahp_words.txt")
        with self.assertRaises(FileNotFoundError):
            conc.load_concordance_table("diclaration.txt")

if __name__ == '__main__':
    unittest.main()
