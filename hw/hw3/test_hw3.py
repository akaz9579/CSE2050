import unittest
from hw3 import *

class TestHW3(unittest.TestCase):

    def test_generate_lists(self):
        """"""
        size = 10
        list1, list2 = generate_lists(size)
        self.assertEqual(len(list1), size)
        self.assertEqual(len(list2), size)
        self.assertEqual(len(set(list1)), size)  
        self.assertEqual(len(set(list2)), size)  

    def test_find_common(self):
        """ """
        list1 = [1, 2, 3, 4, 5]
        list2 = [4, 5, 6, 7, 8]
        result = find_common(list1, list2)
        self.assertEqual(result, 2)  
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        result = find_common(list1, list2)
        self.assertEqual(result, 0)  

    def test_find_common_efficient(self):
        """ """
        list1 = [1, 2, 3, 4, 5]
        list2 = [4, 5, 6, 7, 8]
        result = find_common_efficient(list1, list2)
        self.assertEqual(result, 2)  

        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        result = find_common_efficient(list1, list2)
        self.assertEqual(result, 0)  

if __name__ == "__main__":
    unittest.main()
