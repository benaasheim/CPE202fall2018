class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __eq__(self, other):
        return (self.data == other) or (self.data == other.data)
class Stack:
    def __init__(self, capacity):
        '''Creates and empty stack with a capacity'''
        self.capacity = capacity
        self.head = None
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
            new = Node(item)
            new.next = self.head
            self.head = new
            self.num_items += 1
    
    def pop(self): 
        '''If stack is not empty, pops item from stack and returns item.
           If stack is empty when pop is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.is_empty():
            raise IndexError
        else:
            a = self.head
            self.head = (self.head).next
            self.num_items -= 1
            return a
    
    def peek(self):
        '''If stack is not empty, returns next item to be popped (but does not pop the item)
           If stack is empty, raises IndexError
           MUST have O(1) performance'''
        if self.is_empty():
            raise IndexError()
        else:
            return self.head

    def size(self):
        return self.num_items
