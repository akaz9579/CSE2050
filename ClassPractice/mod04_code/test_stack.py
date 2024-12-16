from stack import Stack
import unittest

class TestStack(unittest.TestCase):
    def test_init(self):
        """Creates an empty stack and tests length and is_empty()"""
        s = Stack()
        self.assertEqual(len(s), 0)
        self.assertTrue(s.is_empty())

    def test_push_pop(self):
        """Adds 10 items, then removes them."""
        s = Stack()
        n = 10

        for i in range(n):
            s.push(i) # add i to the stack
            self.assertEqual(s.peek(), i)
            self.assertFalse(s.is_empty())
            self.assertEqual(len(s), i+1)

        for i in range(n):
            self.assertEqual(s.peek(), n-1-i)
            self.assertFalse(s.is_empty())
            self.assertEqual(s.pop(), n-1-i)
            
            self.assertEqual(len(s), n-i-1)

        self.assertTrue(s.is_empty())
            


unittest.main()