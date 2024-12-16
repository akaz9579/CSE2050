from linkedlist import node
import unittest

class TestNode(unittest.TestCase):
    def test_init_one(self):
        n1 = node('jake')

        self.assertEqual(n1.data, 'jake')
        self.assertEqual(n1.link, None)

    def test_initIthree(self):
        n1 = node('jake')
        n2 = node('racheal')
        n3 = node('cassie')

        n1.link = n2
        n2.link = n3

        self.assertIs(n1.link,n2)
        self.assertIs(n1.link.link,n3)
        self.assertIs(n1.link.link.link, None)


if __name__ == '__main__':
    unittest.main()
