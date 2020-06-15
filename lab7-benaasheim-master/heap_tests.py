import unittest
from heap import *

class TestHeap(unittest.TestCase):

    def test_01_enqueue(self):
        test_heap = MaxHeap(7)
        x = test_heap.dequeue()
        self.assertEqual(x, None)
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.peek(), 9)
        insert = test_heap.enqueue(10)
        self.assertTrue(insert)
        insert = test_heap.enqueue(10)
        self.assertFalse(insert)
        self.assertEqual(test_heap.contents(), [10, 6, 9, 2, 5, 7, 8])
        self.assertEqual(test_heap.peek(), 10)

    def test_02_dequeue(self):
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.dequeue(), 9)
        self.assertEqual(test_heap.get_size(), 5)
        self.assertEqual(test_heap.contents(), [8, 6, 7, 2, 5])

    def test_03_heap_contents(self):
        test_heap = MaxHeap(8)
        test_heap.build_heap([1, 2, 3])
        self.assertEqual(test_heap.contents(), [3, 2, 1])

    def test_04_build_heap(self):
        test_heap = MaxHeap(8)
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.contents(), [9, 6, 8, 2, 5, 7])

    def test_05_is_empty(self):
        test_heap = MaxHeap(5)
        self.assertTrue(test_heap.is_empty())

    def test_06_is_full(self):
        test_heap = MaxHeap(5)
        built = test_heap.build_heap([1, 2, 3, 4, 5])
        self.assertTrue(test_heap.is_full())

    def test_07_get_heap_cap(self):
        test_heap = MaxHeap(7)
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        insert = test_heap.enqueue(10)
        self.assertEqual(test_heap.get_capacity(), 7)

    def test_08_get_size(self):
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.get_size(), 6)

    def test_09_perc_down(self):
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 8, 6, 5, 7])
        test_heap.perc_down(1)
        self.assertEqual(test_heap.contents(), [9, 6, 8, 2, 5, 7])

    def test_10_perc_up(self):
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 8, 6, 5, 7])
        test_heap.perc_up(6)
        self.assertEqual(test_heap.contents(), [9, 6, 8, 2, 5, 7])

    def test_11_heap_sort_ascending(self):
        test_heap = MaxHeap()
        list1 = [2, 9, 7, 6, 5, 8]
        test_heap.heap_sort_ascending(list1)
        self.assertEqual(test_heap.contents(), [2, 5, 6, 7, 8, 9])

    def test_12_build_heap(self):
        test_heap = MaxHeap(3)
        test_heap.build_heap([2, 9, 8, 6, 5, 7])
        self.assertEqual(test_heap.contents(), [9, 6, 8, 2, 5, 7])

    def test_13_build_heap(self):
        test_heap = MaxHeap(3)
        test_heap.build_heap([10, 7, 3, 2, 4, 5, 8, 1, 6, 15])
        self.assertEqual(test_heap.contents(), [15, 10, 8, 6, 7, 5, 3, 1, 2, 4])

    def test_14_build_heap(self):
        test_heap = MaxHeap(3)
        test_heap.build_heap([15, 10, 8, 6, 5, 7, 3, 1, 2, 4])
        self.assertEqual(test_heap.contents(), [15, 10, 8, 6, 5, 7, 3, 1, 2, 4])

    def test_15_build_heap(self):
        test_heap = MaxHeap(3)
        test_heap.build_heap([8, 6, 10, 1, 4, 5, 3, 7, 2, 15])
        self.assertEqual(test_heap.contents(), [15, 8, 10, 7, 6, 5, 3, 1, 2, 4])

    def test_16_build_heap(self):
        test_heap = MaxHeap(3)
        test_heap.build_heap([8, 6, 10, 3, 1, 5, 4, 7, 2, 9, 0])
        self.assertEqual(test_heap.contents(), [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
        test_heap.heap_sort_ascending(test_heap.contents())
        self.assertEqual(test_heap.contents(), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


if __name__ == "__main__":
    unittest.main()
