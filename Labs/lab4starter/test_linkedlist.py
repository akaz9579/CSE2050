import unittest
from linkedlist import Node, LinkedList

class TestNode(unittest.TestCase):
    def test1(self):
        node1 = Node("we" )
        self.assertEqual(node1.item, "we") 
        self.assertEqual(node1.link, None )

    def testRepr(self):
        node1 = Node("we")
        self.assertEqual(repr(node1), "Node(we)")
 

class TestLinkedList(unittest.TestCase):

    def testEmpty(self):

        ll = LinkedList()
        self.assertEqual(ll._len, 0) 
        self.assertEqual(ll.get_head(), None )
        self.assertEqual(ll.get_tail(), None )

    def test_AddLast(self):
        ll = LinkedList()
        for x in range(3):
            ll.add_last(x)
        self.assertEqual(ll._len, 3) 
        self.assertEqual(ll.get_head(), 0)
        self.assertEqual(ll.get_tail(), 2 )

    def test_remove_empty(self):
        ll = LinkedList()
        with self.assertRaises(RuntimeError):
            ll.remove_last()


if __name__ == '__main__':
    unittest.main()