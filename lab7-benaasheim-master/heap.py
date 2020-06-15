class MaxHeap:

    def __init__(self, capacity=50):
        """Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created."""
        self.capacity = capacity
        self.heap = [None]*(capacity + 1)
        self.num_items = 0

    def enqueue(self, item):
        """inserts "item" into the heap, returns true if successful, false if there is no room in the heap"""
        if self.is_full():
            return False
        else:
            self.num_items += 1
            self.heap[(self.get_size())] = item
            self.perc_up(self.get_size())
            return True

    def peek(self):
        """returns max without changing the heap, returns None if the heap is empty"""
        return self.heap[1]

    def dequeue(self):
        """returns max and removes it from the heap and restores the heap property
           returns None if the heap is empty"""
        if self.is_empty():
            return None
        else:
            retval = self.heap[1]
            self.heap[1] = self.heap[self.num_items]
            self.heap[self.num_items] = None
            self.num_items -= 1
            for i in range(1, self.num_items):
                self.perc_down(i)
            return retval

    def contents(self):
        """returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)"""
        return self.heap[1:(self.num_items+1)]

    def build_heap(self, alist):
        """Builds a heap from the items in alist and builds a heap using the bottom up method.
        If the capacity of the current heap is less than the number of
        items in alist, the capacity of the heap will be increased"""
        if len(alist) > self.capacity:
            self.capacity = len(alist)
            self.heap = [None]*(len(alist) + 2)
        for n in range(len(alist)):
            self.heap[n+1] = alist[n]
        self.num_items = len(alist)
        for i in range(self.num_items//2, 0, -1):
            self.perc_down(i)

    def is_empty(self):
        """returns True if the heap is empty, false otherwise"""
        return self.num_items == 0

    def is_full(self):
        """returns True if the heap is full, false otherwise"""
        return self.num_items == self.capacity

    def get_capacity(self):
        """this is the maximum number of a entries the heap can hold
        1 less than the number of entries that the array allocated to hold the heap can hold"""
        return self.capacity

    def get_size(self):
        """the actual number of elements in the heap, not the capacity"""
        return self.num_items

    def perc_down(self, i):
        """where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        print(self.heap, i, self.heap[i])
        if i <= (self.num_items//2):
            if (self.heap[2*i] != None) and (self.heap[2*i+1] != None) and (self.heap[i] < self.heap[2*i]) and (self.heap[i] < self.heap[2*i+1]):
                if self.heap[2*i] < self.heap[2*i+1]:
                    self.swap(i, (2*i+1))
                    self.perc_down(2*i+1)
                else:
                    self.swap(i, (2*i))
                    self.perc_down(2*i)
            elif (self.heap[2*i] != None) and (self.heap[i] < self.heap[2*i]):
                self.swap(i, (2*i))
                self.perc_down(2*i)
            elif (self.heap[2*i+1] != None) and (self.heap[i] < self.heap[2*i+1]):
                self.swap(i, (2*i+1))
                self.perc_down(2*i+1)

    def perc_up(self, i):
        """where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        if i >= 2:
            if self.heap[i] > self.heap[i//2]:
                self.swap(i, i//2)
                self.perc_up(i//2)

    def heap_sort_ascending(self, alist):
        """perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, then mutate alist to put the items in ascending order"""
        self.build_heap(alist)
        self.selection_sort()

    def swap(self, a, b):
        x = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = x

    def selection_sort(self):
        placemark = 1
        lowest = self.heap[1]
        lowin = 1
        while placemark < self.num_items +1:
            lowest = self.heap[placemark]
            lowin = placemark
            for s in range(lowin, (self.num_items+1)):
                if self.heap[s] < lowest:
                    lowest = self.heap[s]
                    lowin = s
            self.swap(placemark, lowin)
            placemark += 1
