from hash_quad import *
import string

class Concordance:

    def __init__(self):
        self.stop_table = None          # hash table for stop words
        self.concordance_table = None   # hash table for concordance
    

    def load_stop_table(self, filename):
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        self.stop_table = HashTable(191)
        try:
            a = open(filename, "r")
            lines = a.readlines()
            a.close()
        except:
            raise FileNotFoundError()
        for n in range(len(lines)):
            self.stop_table.insert(lines[n][:-1], n)

    def load_concordance_table(self, filename):
        """ Read words from input text file (filename) and insert them into the concordance hash table, 
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
        Starting size of hash table should be 191: self.concordance_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        self.concordance_table = HashTable(191)
        try:
            a = open(filename, "r")
            lines = a.readlines()
            a.close()
        except:
            raise FileNotFoundError()
        for n in range(len(lines)):
            lone = clean(lines[n])
            line = lone.split(" ")
            for i in line:
                if (i != None) and (self.stop_table.in_table(i) == False) and (i != ""):
                    self.concordance_table.insert(i, n+1)
    def write_concordance(self, filename):
        """ Write the concordance entries to the output file(filename)
        See sample output files for format."""
        all_keys = self.concordance_table.get_all_keys()
        lines = []
        for i in all_keys:
            a = ""
            a += i + ":"
            f = self.concordance_table.get_value(i)
            if f != None:
                for s in f:
                    a += " " + str(s)
            a += "\n"
            lines.append(a)
        a = open(filename, "w+")
        for i in lines:
            a.write(i)
        a.close()

def clean(string):
    new = ""
    verboten = '"' + ",.~`'\t\n1234567890_+=|}{][><!@#$%^&*()?/:;"
    for i in string:
        if i not in verboten:
            if i == "-":
                new += " "
            elif (ord(i) < 97) and (ord(i) >= 65):
                new += chr(ord(i)+32)
            else:
                new += i
    return new
