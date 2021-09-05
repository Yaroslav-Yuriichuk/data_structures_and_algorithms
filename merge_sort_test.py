from sys import float_repr_style
import unittest
import random
from merge_sort.merge_sort import MergeSort

class TestMergeSort(unittest.TestCase):
    NUMBER_OF_TESTS_PER_TEST_CASE = 10
    ELEMENTS_NUMBER = 20

    """
    @staticmethod
    def is_sorted(arr, reverse=False):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1] and not reverse \
                or arr[i] < arr[i+1] and reverse:
                return False
        return True       
    """

    def test_average_case_asc(self):
        for _ in range(TestMergeSort.NUMBER_OF_TESTS_PER_TEST_CASE):
            arr = [random.randint(0, 100) for _ in range(TestMergeSort.ELEMENTS_NUMBER)]
            MergeSort.sort(arr)
            # self.assertTrue(TestMergeSort.is_sorted(arr))
            self.assertEqual(arr, sorted(arr))

    def test_average_case_desc(self):
        for _ in range(TestMergeSort.NUMBER_OF_TESTS_PER_TEST_CASE):
            arr = [random.randint(0, 100) for _ in range(TestMergeSort.ELEMENTS_NUMBER)]
            MergeSort.sort(arr, reverse=True)
            # self.assertTrue(TestMergeSort.is_sorted(arr, reverse=True))
            self.assertEqual(arr, sorted(arr, reverse=True))

    def test_asc_array_acs_order(self):
        for _ in range(TestMergeSort.NUMBER_OF_TESTS_PER_TEST_CASE):
            arr = [random.randint(i * 5, (i + 1) * 5) for i in range(TestMergeSort.ELEMENTS_NUMBER)]
            MergeSort.sort(arr)
            self.assertEqual(arr, sorted(arr))

    def test_asc_array_desc_order(self):
        for _ in range(TestMergeSort.NUMBER_OF_TESTS_PER_TEST_CASE):
            arr = [random.randint(i * 5, (i + 1) * 5) for i in range(TestMergeSort.ELEMENTS_NUMBER)]
            MergeSort.sort(arr, reverse=True)
            self.assertEqual(arr, sorted(arr, reverse=True))

    def test_desc_array_asc_order(self):
        for _ in range(TestMergeSort.NUMBER_OF_TESTS_PER_TEST_CASE):
            arr = [random.randint(100 - (i + 1) * 5, 100 - i * 5) for i in range(TestMergeSort.ELEMENTS_NUMBER)]
            MergeSort.sort(arr)
            self.assertEqual(arr, sorted(arr))

    def test_desc_array_decs_order(self):
        for _ in range(TestMergeSort.NUMBER_OF_TESTS_PER_TEST_CASE):
            arr = [random.randint(100 - (i + 1) * 5, 100 - i * 5) for i in range(TestMergeSort.ELEMENTS_NUMBER)]
            MergeSort.sort(arr, reverse=True)
            self.assertEqual(arr, sorted(arr, reverse=True))
