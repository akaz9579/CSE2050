from linkedlist import Node, LinkedList
import unittest

class TestLinkedList(unittest.TestCase):
    def TestINIT(self):
        ll1 =LinkedList()
        self.assertEqual(len(ll1),0)
        self.assertIsNone(ll1.get_head())
        self.assertIsNone(ll1.get_tail())

    def testAddFirst(self):
        ll1 = LinkedList()

        ll1.add_first("rachael")
        self.assertEqual(ll1.get_head().data, 'racheal')
        self.assertEqual(ll1.get_head().data, 'racheal')




if __name__ == '__main__':
    pass