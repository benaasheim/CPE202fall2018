class OrderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        if self.head == None:
            self.head = Node(item)
        elif self.head.item > item:
            a = self.head
            self.head = Node(item)
            self.head.next = a
            a.prev = self.head
        elif self.head.item == item:
            self.head.item = item
        else:
            self.head._add(item)

    def remove(self, item):
        if self.head.item == item:
            self.head = self.head.next
            return True
        elif self.head.next == None:
            return False
        else:
            return self.head.next._remove(item)

    def index(self, item):
        if self.head.item == item:
            return 0
        else:
            return self.head.next._index(item, 1)

    def pop(self, index):
        if index == 0:
            a = self.head.item
            self.head = self.head.next
            return a
        else:
            return self.head.next._pop((index-1))

    def search(self, item):
        if self.head.item == item:
            return True
        else:
            return self.head._search(item)

    def python_list(self):
        if self.head == None:
            return []
        elif self.head.next == None:
            return [self.head.item]
        else:
            return [self.head.item] + self.head.next._pl([self.head.item])

    def python_list_reversed(self):
        if self.head == None:
            return []
        elif self.head.next == None:
            return [self.head.item]
        else:
            return self.head.next._plr([self.head.item]) + [self.head.item]

    def size(self):
        if self.head == None:
            return 0
        else:
            return self.head._sz(1)

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

    def _add(self, item):
        if self.next == None:
            self.next = Node(item)
            self.next.prev = self
        elif self.item == item:
            self.item = item
        elif self.next.item > item:
            self.next.prev = Node(item)
            self.next.prev.next = self.next
            self.next = self.next.prev
            self.next.prev = self
        else:
            self.next._add(item)

    def _remove(self, item):
        if self.item == item:
            if self.next != None:
                self.prev.next = self.next
                self.next.prev = self.prev
                return True
            else:
                self.prev.next = None
                return True
        elif self.next == None:
            return False
        else:
            return self.next._remove(item)

    def _index(self, item, count):
        if self.item == item:
            return count
        else:
            return self.next._index(item, (count+1))

    def _pop(self, index):
        print(index, self.item, self.next.item, self.prev)
        if index == 0:
            a = self.item
            self.next.prev = self.prev
            self.prev.next = self.next
            return a
        else:
            return self.next._pop((index-1))

    def _search(self, item):
        if self.item == item:
            return True
        elif self.next == None:
            return False
        else:
            return self.next._search(item)

    def _plr(self, lis):
        if self.next == None:
            return [self.item]
        else:
            return self.next._plr(lis) + [self.item]

    def _sz(self, count):
        if self.next == None:
            return count
        else:
            return self.next._sz(count+1)

    def _pl(self, lis):
        if self.next == None:
            return [self.item]
        else:
            return [self.item] + self.next._pl(lis)

