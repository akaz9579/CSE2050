import unittest
from process import Process

class TestProcess(unittest.TestCase):
    def test_nameOnly(self):
        """"""
        p1= Process("john")
        p2 = Process(None)

        self.assertEqual(p1.pid, "john")
        self.assertEqual(p2.pid, None)
    
    def test_NameWCycle(self):
        """tests if cycle is updated"""
        p1=Process("john",10)
        p2 = Process("bob")

        self.assertEqual(p1.pid, "john")
        self.assertEqual(p1.cycles, 10)
        self.assertEqual(p2.pid, "bob")
        self.assertEqual(p2.cycles, 100)
    
    def test_repr(self):
        """test repr method"""
        p1 = Process("john", 10)
        p2 = Process("bob")

        self.assertEqual(repr(p1), "Process(john,10)")
        self.assertEqual(repr(p2), "Process(bob,100)")

    

    def test_eq(self):
        """test equality based only on pid"""
        p1 = Process("john", 10)
        p2 = Process("john", 20)  
        p3 = Process("bob", 10)   

        self.assertEqual(p1, p2)   
        self.assertNotEqual(p1, p3)  
        


        


if __name__ == '__main__':
    unittest.main()


