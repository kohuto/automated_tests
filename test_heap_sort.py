import unittest
from heap_sort import heapSort

class TestHeapSort(unittest.TestCase):

    def test_heap_sort(self):
        arr = [12, 11, 13, 5, 6, 7]
        heapSort(arr)
        self.assertEqual(arr, [5, 6, 7, 11, 12, 13])

    def test_empty_list(self):
        arr = []
        heapSort(arr)
        self.assertEqual(arr, [])

    def test_sorted_list(self):
        arr = [1, 2, 3, 4, 5]
        heapSort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_list(self):
        arr = [5, 4, 3, 2, 1]
        heapSort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()
