import unittest
from hw6 import bubble_sort, selection_sort, insertion_sort, merge

class SortingTestFactory:
    """This class provides methods to generate test cases for sorting algorithms."""
    def setUp(self, sorting_alg):
        """
        Set up the sorting algorithm for testing.
        Args:
            sorting_alg (function): The sorting algorithm to be tested.
        """
        self.sorting_alg = sorting_alg

    def test_merge(self):
        """ Test case for the merge function to verify that it correctly merges three sorted rows."""
        # Define the sorted rows to test
        matrix = [[1, 4, 7, 10], [2, 5, 8, 11],[3, 6, 9, 12]] 
        # Expected merged result
        expected_merged = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

        # Call the merge function
        self.assertEqual(expected_merged, merge(matrix[0],matrix[1],matrix[2]))

    def is_sorted(self, L):
        """ Check if a list is sorted. """
        return all(L[i] <= L[i + 1] for i in range(len(L) - 1))

    def test_empty(self):
        """TODO"""
        matrix = [[],[],[]]
        sorted_row, n_swaps = self.sorting_alg(matrix)
        self.assertEqual(sorted_row, [])
        self.assertEqual(n_swaps, 0)
    
    def test_sorted(self):
        """TODO"""
        matrix = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]  
        sorted_row, n_swaps = self.sorting_alg(matrix)
        self.assertTrue(self.is_sorted(sorted_row))
        self.assertEqual(n_swaps, 0)  

    def test_reverse_sorted(self):
        """TODO"""
        matrix = [[5, 4, 3, 2, 1], [5, 4, 3, 2, 1], [5, 4, 3, 2, 1]]  # Reverse sorted rows for testing
        sorted_row, n_swaps = self.sorting_alg(matrix)
        self.assertTrue(self.is_sorted(sorted_row))

        if self.sorting_alg == bubble_sort:
            self.assertEqual(n_swaps, 10) 
        elif self.sorting_alg == insertion_sort:
            self.assertEqual(n_swaps, 10)  
        elif self.sorting_alg == selection_sort:
            self.assertEqual(n_swaps, 2)  

    def test_random(self):
        """TODO"""
        matrix = [[3, 1, 4, 5, 2], [9, 7, 8, 6, 10], [12, 11, 13, 15, 14]]  # Random rows for testing
        sorted_row, n_swaps = self.sorting_alg(matrix)
        self.assertTrue(self.is_sorted(sorted_row))

        if self.sorting_alg == bubble_sort:
            self.assertEqual(n_swaps, 4)  
        elif self.sorting_alg == insertion_sort:
            self.assertEqual(n_swaps, 5)  
        elif self.sorting_alg == selection_sort:
            self.assertEqual(n_swaps, 2)  

    

class TestBubble(SortingTestFactory, unittest.TestCase):
    """Test class for the bubble sort algorithm."""

    def setUp(self):
        """Set up the bubble sort algorithm for testing."""
        super().setUp(bubble_sort)


class TestInsertion(SortingTestFactory, unittest.TestCase):
    """TODO"""
    def setUp(self):
        """Set up the insertion sort algorithm for testing."""
        super().setUp(insertion_sort)


class TestSelection(SortingTestFactory, unittest.TestCase):
    """TODO"""
    def setUp(self):
        """Set up the selection sort algorithm for testing."""
        super().setUp(selection_sort)

if __name__ == "__main__":
    unittest.main()
