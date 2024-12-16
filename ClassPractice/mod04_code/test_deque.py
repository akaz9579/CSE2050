from deque import Deque
import unittest

class TestDeque(unittest.TestCase):
    def test_init(self):
        """Creates an empty deque and tests attributes"""
        d = Deque()
        self.assertTrue(d.is_empty())
        self.assertEqual(len(d), 0)

    def test_add_first_remove_last(self):
        """Adds 10 items to front, then removes 10 items from end."""
        d = Deque()
        n = 10

        for i in range(n):
            d.add_first(i)
            self.assertFalse(d.is_empty())
            self.assertEqual(len(d), i+1)

        for i in range(n):
            self.assertEqual(d.remove_last(), i)
            self.assertEqual(len(d), n-1-i)

        self.assertTrue(d.is_empty())
        
    def test_add_last_remove_first(self):
        """Adds 10 items to back, then removes 10 items from front."""
        d = Deque()
        n = 10

        for i in range(n):
            d.add_last(i)
            self.assertFalse(d.is_empty())
            self.assertEqual(len(d), i+1)

        for i in range(n):
            self.assertEqual(d.remove_first(), i)
            self.assertEqual(len(d), n-1-i)

        self.assertTrue(d.is_empty())

    def test_add_first_remove_first(self):
        """Adds 10 items to front, then removes 10 items from front"""
        d = Deque()
        n = 10

        for i in range(n):
            d.add_first(i)
            self.assertFalse(d.is_empty())
            self.assertEqual(len(d), i+1)

        for i in range(n):
            self.assertEqual(d.remove_first(), n-1-i)
            self.assertEqual(len(d), n-1-i)

        self.assertTrue(d.is_empty())

    def test_add_last_remove_last(self):
        """Adds 10 items to front, then removes 10 items from front"""
        d = Deque()
        n = 10

        for i in range(n):
            d.add_last(i)
            self.assertFalse(d.is_empty())
            self.assertEqual(len(d), i+1)

        for i in range(n):
            self.assertEqual(d.remove_last(), n-1-i)
            self.assertEqual(len(d), n-1-i)

        self.assertTrue(d.is_empty())

unittest.main()