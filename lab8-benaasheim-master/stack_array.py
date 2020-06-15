from operator import itemgetter, attrgetter
class Stack:
    '''Implements an efficient last-in first-out Abstract Data Type using a Python List'''
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None]*capacity
        self.num_items = 0 
    def is_empty(self):
        return self.num_items == 0
    def is_full(self):
        return self.num_items == self.capacity
    def push(self, item):
        '''If stack is not full, pushes item on stack. 
           If stack is full when push is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.is_full():
            raise IndexError()
        else:
            self.items[self.num_items] = item
            self.num_items += 1
    def pop(self): 
        '''If stack is not empty, pops item from stack and returns item.
           If stack is empty when pop is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.is_empty():
            raise IndexError()
        else:
            ret = self.items[self.num_items - 1]
            self.items[self.num_items - 1] = None
            self.num_items -= 1
            return ret
    def peek(self):
        '''If stack is not empty, returns next item to be popped (but does not pop the item)
           If stack is empty, raises IndexError
           MUST have O(1) performance'''
        if self.is_empty():
            raise IndexError()
        else:
            return self.items[self.num_items - 1]
    def size(self):
        '''Returns the number of elements currently in the stack, not the capacity
           MUST have O(1) performance'''
        return self.num_items
    def sorter(self):
        a = self.items[0:self.num_items]
        sorted(a, key=attrgetter("id"), reverse=True)
        b = self.items[self.num_items:]
        self.items = a + b