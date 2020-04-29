import unittest
from numpy import array
import numpy.testing as npt
from algpy.sort.insertionsort import insertion_sort

class TestInsertionSort(unittest.TestCase):
    def test_emptylist_returns_emptylist(self):
        empty_array = array([])
        result = insertion_sort(empty_array)
        npt.assert_array_equal(result, empty_array)

    def test_singleelement_returns_singleelement(self):
        single_element_array = array([1])
        result = insertion_sort(single_element_array)
        npt.assert_array_equal(result, single_element_array)

    def test_small_unsorted_returns_small_sorted(self):
        small_unsorted_element_array = array([31, 41, 59, 26, 41, 58])
        small_sorted_element_array = array([26, 31, 41, 41, 58, 59])
        result = insertion_sort(small_unsorted_element_array)
        npt.assert_array_equal(result, small_sorted_element_array)


if __name__ == '__main__':
    unittest.main()
