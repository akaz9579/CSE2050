from searches import linear_search, binary_search_recr, binary_search_iter
import unittest

class TestSearchFactory:
    def setUp(self, search_alg):
        self.search_alg = search_alg

    def test_true_100(self):
        """Ensures we can find an item at any position in lists up to 100 items"""
        for n in range(100):
            L = [i for i in range(n)]

            for item in range(n):
                self.assertTrue(self.search_alg(item, L))

    def test_false_100(self):
        """Ensures that any items not in L return False"""
        for n in range(100):
            L = [i for i in range(n)]

            self.assertFalse(self.search_alg(-1, L))

            for item in range(n):
                self.assertFalse(self.search_alg(item+0.5, L))

    def test_empty(self):
        """Ensures algorithm works on empty list"""
        self.assertFalse(self.search_alg(0, []))

class TestLinearSearch(TestSearchFactory, unittest.TestCase):
    def setUp(self):
        """Passes search alg to factory"""
        return TestSearchFactory.setUp(self, linear_search)
    
class TestBinarySearchRecr(TestSearchFactory, unittest.TestCase):
    def setUp(self):
        """Passes search alg to factory"""
        return TestSearchFactory.setUp(self, binary_search_recr)
    
class TestBinarySearchIter(TestSearchFactory, unittest.TestCase):
    def setUp(self):
        """Passes search alg to factory"""
        return TestSearchFactory.setUp(self, binary_search_iter)
if __name__ == '__main__':
    unittest.main()