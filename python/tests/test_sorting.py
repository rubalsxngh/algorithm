import unittest
from data_structs.sorting import merge_sort
from data_structs.sorting import quick_sort

class test_merge_sort(unittest.TestCase):
    def test_merge(self):
        input_arr= [50, 60, 30, 20, 10]
        sorted_ans= [10, 20, 30, 50, 60]

        sorted_arr= merge_sort.merge(input_arr, 0, len(input_arr)-1)

        self.assertEqual(sorted_arr, sorted_ans)

class test_merge_sort(unittest.TestCase):
    def test_merge(self):
        input_arr= [50, 60, 30, 20, 10]
        sorted_ans= [10, 20, 30, 50, 60]

        sorted_arr= quick_sort.quick(input_arr, 0, len(input_arr)-1)

        self.assertEqual(sorted_arr, sorted_ans)