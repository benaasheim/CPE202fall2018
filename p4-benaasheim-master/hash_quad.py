class HashTable:

    def __init__(self, table_size):         # can add additional attributes
        self.table_size = table_size        # initial table size
        self.hash_table = [None]*table_size # hash table
        self.num_items = 0                  # empty hash table

    def insert(self, key, value):
        """ Inserts an entry into the hash table (using Horner hash function to determine index, and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value is the line number that the word appears on. 
        If the key is not already in the table, then the key is inserted, and the value is used as the first line number in the list of line numbers. 
        If the key is in the table, then the value is appended to that keys list of line numbers. 
        If value is not used for a particular hash table (e.g. the stop words hash table), can use the default of 0 for value and just call the insert function with the key.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased (doubled + 1)."""
        if not self.in_table(key):
            self.num_items += 1
            if self.get_load_factor() > 0.5:
                table_size = self.get_table_size()
                self.table_size = (2*table_size)+1
                temp = []
                for i in self.hash_table:
                    if i != None:
                        temp.append(i)
                self.hash_table = [None]*self.table_size
                self.num_items = 1
                for i in temp:
                    for n in i[1]:
                        self.insert(i[0], n)
            keyy = self.horner_hash(key)
            counter = 0
            while self.hash_table[keyy%self.table_size] != None:
                keyy -= (counter**2)
                counter += 1
                keyy += (counter**2)
            self.hash_table[keyy%self.table_size] = (key, [value])
        else:
            ind = self.get_index(key)
            ccc = False
            for i in self.hash_table[ind][1]:
                if i == value:
                    ccc = True
            if ccc == False:
                self.hash_table[ind][1].append(value)
                self.hash_table[ind][1].sort()

    def horner_hash(self, key):
        """ Compute and return an integer from 0 to the (size of the hash table) - 1
        Compute the hash value by using Horners rule, as described in project specification."""
        if len(key) > 8:
            n = 8
        else:
            n = len(key)
        hh = 0
        for s in range(n):
            hh += (ord(key[s])) * (31**(n-1-s))
        return hh%self.table_size

    def in_table(self, key):
        """ Returns True if key is in an entry of the hash table, False otherwise."""
        if self.num_items == 0:
            return False
        else:
            keyy = self.horner_hash(key)
            counter = 0
            while (self.hash_table[keyy%self.table_size] != None) and (self.hash_table[keyy%self.table_size][0] != key):
                keyy -= (counter**2)
                counter += 1
                keyy += (counter**2)
            if self.hash_table[keyy%self.table_size] == None:
                return False
            else:
                return True
        #return (self.hash_table[self.horner_hash(key)] != None) and (self.hash_table[self.horner_hash(key)][0] == key)

    def get_index(self, key):
        """ Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None."""
        if self.num_items == 0:
            return None
        else:
            keyy = self.horner_hash(key)
            counter = 0
            while (self.hash_table[keyy%self.table_size] != None) and (self.hash_table[keyy%self.table_size][0] != key):
                keyy -= (counter**2)
                counter += 1
                keyy += (counter**2)
            if self.hash_table[keyy%self.table_size] == None:
                return None
            else:
                return keyy
       # if not self.in_table(key):
       #     return None
       # else:
       #     return self.horner_hash(key)

    def get_all_keys(self):
        """ Returns a Python list of all keys in the hash table."""
        klis = []
        if self.num_items > 0:
            for i in self.hash_table:
                if i != None:
                    klis.append(i[0])
        klis.sort()
        return klis

    def get_value(self, key):
        """ Returns the value (list of line numbers) associated with the key. 
        If key is not in hash table, returns None."""
        if self.num_items == 0:
            return None
        if not self.in_table(key):
            return None
        else:
            return self.hash_table[self.get_index(key)][1]

    def get_num_items(self):
        """ Returns the number of entries (words) in the table."""
        return self.num_items

    def get_table_size(self):
        """ Returns the size of the hash table."""
        return self.table_size

    def get_load_factor(self):
        """ Returns the load factor of the hash table (entries / table_size)."""
        return self.get_num_items() / self.get_table_size()
