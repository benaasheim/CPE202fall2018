import unittest
from queue_array import Queue
#from queue_linked import Queue

class TestLab1(unittest.TestCase):
    def test_queue(self):
        '''Trivial test to ensure method names and parameters are correct'''
        q = Queue(5)
        q.is_empty()
        q.is_full()
        q.enqueue('thing')
        q.dequeue()
        q.size()
    
    def test_queue2(self):
        q = Queue(5)
        self.assertTrue(q.is_empty())
        q.enqueue(5)
        self.assertFalse(q.is_empty())
        self.assertFalse(q.is_full())
        q.enqueue(5)
        q.enqueue(5)
        q.enqueue(5)
        q.enqueue(5)
        with self.assertRaises(IndexError):
            q.enqueue(5)
        q.dequeue()
        q.dequeue()
        q.dequeue()
        q.dequeue()
        self.assertEqual(q.size(), 1)
        q.dequeue()
        self.assertTrue(q.is_empty())
        with self.assertRaises(IndexError):
            q.dequeue()
if __name__ == '__main__': 
    unittest.main()
