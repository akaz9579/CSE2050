import unittest
import random
random.seed(658)  # Fixing the random seed to guarantee behavior on random tests
from magicsort import magic_insertionsort, magic_mergesort, magic_quicksort

class TestMagicBoundedSort:
    """Test Factory for insertion, merge, and quick sorts only on a sublist"""

    def test_empty_list(self):
        """Tests sorting algorithm on an empty list"""
        L = []
        expected_output = []
        self.sorting_alg(L, 0, len(L))
        self.assertEqual(L, expected_output)

    def test_whole_list(self):
        """Tests sorting algorithm on a full 5-item list"""
        L = list(reversed(range(5)))
        expected_output = list(range(5))
        self.sorting_alg(L, 0, len(L))
        self.assertEqual(L, expected_output)

    def test_middle_of_list(self):
        """Tests sorting algorithm on the middle section of a 20-item list"""
        L = list(reversed(range(20)))
        left = 5
        right = 15
        first_half = L[:left]              # Unsorted first section
        sorted_middle = sorted(L[left:right])  # Expected sorted middle section
        second_half = L[right:]            # Unsorted last section
        expected_output = first_half + sorted_middle + second_half
        self.sorting_alg(L, left, right)
        self.assertEqual(L, expected_output)

    def test_random_lists_and_bounds(self):
        """Tests sorting algorithm on various random lists with random bounds"""
        for _ in range(20):
            N = random.randint(75, 100)
            L = list(reversed(range(N)))
            left = random.randint(0, N // 2)
            right = random.randint(left, N)
            first_half = L[:left]
            sorted_middle = sorted(L[left:right])
            second_half = L[right:]
            expected_output = first_half + sorted_middle + second_half
            self.sorting_alg(L, left, right)
            self.assertEqual(L, expected_output)

    def test_single_element_bound(self):
        """Tests sorting algorithm on a sublist of a single element"""
        L = [5, 2, 9, 1, 6]
        expected_output = L.copy()  # Single-element sort should not alter list
        self.sorting_alg(L, 2, 3)
        self.assertEqual(L, expected_output)

    def test_adjacent_elements(self):
        """Tests sorting algorithm on adjacent elements in a list"""
        L = [5, 2, 9, 1, 6]
        expected_output = [5, 2, 1, 9, 6]  # Only adjacent 9 and 1 sorted
        self.sorting_alg(L, 2, 4)
        self.assertEqual(L, expected_output)


# Test classes for each sorting algorithm
class TestMagicInsertionSort(TestMagicBoundedSort, unittest.TestCase):
    def setUp(self):
        self.sorting_alg = magic_insertionsort

class TestMagicMergeSort(TestMagicBoundedSort, unittest.TestCase):
    def setUp(self):
        self.sorting_alg = magic_mergesort

class TestMagicQuickSort(TestMagicBoundedSort, unittest.TestCase):
    def setUp(self):
        self.sorting_alg = magic_quicksort


if __name__ == "__main__":
    unittest.main()