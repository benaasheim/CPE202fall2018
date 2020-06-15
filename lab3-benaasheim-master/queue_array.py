
class Queue:
    '''Implements an array-based, efficient first-in first-out Abstract Data Type 
       using a Python array (faked using a List)'''

    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None]*capacity
        self.num_items = 0
        '''Creates an empty Queue with a capacity'''

    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise'''
        return self.num_items == 0

    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise'''
        return self.num_items == self.capacity

    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue 
           If Queue is full when enqueue is attempted, raises IndexError'''
        if self.is_full():
            raise IndexError()
        else:
            n = 0
            while self.items[n] != None:
                n += 1
            self.items[n] = item
            self.num_items += 1

    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError'''
        if self.is_empty():
            raise IndexError()
        else:
            x = self.items[0]
            for n in range(len(self.items)-1):
                self.items[n] = self.items[n+1]
            self.items[len(self.items)-1] = None
            self.num_items -= 1
            return x

    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity'''
        return self.num_items