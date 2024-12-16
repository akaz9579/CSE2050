import unittest
from process import Process
from circularqueue import CircularQueue

class TestCircularQueue(unittest.TestCase):
    def test_init(self):
        """Test CircularQueue initialization with and without processes."""
        cq1 = CircularQueue()
        self.assertEqual(len(cq1), 0)

        p1 = Process("john", 5)
        p2 = Process("bob", 10)
        p3 = Process("ron", 15)
        l = [p1, p2, p3]
        cq2 = CircularQueue(l)
        self.assertEqual(len(cq2), 3)
        self.assertEqual(cq2._head.pid, "john")

    def test_add_process(self):
        """Test adding 1, 2, and 3 processes to the CircularQueue."""
        cq1 = CircularQueue()
        p1 = Process("john", 5)
        p2 = Process("bob", 10)
        p3 = Process("ron", 15)

        cq1.add_process(p1)
        self.assertEqual(len(cq1), 1)
        self.assertEqual(cq1._head.pid, "john")

        cq1.add_process(p2)
        self.assertEqual(len(cq1), 2)
        self.assertEqual(cq1._head.link.pid, "bob")

        cq1.add_process(p3)
        self.assertEqual(len(cq1), 3)
        self.assertEqual(cq1._head.link.link.pid, "ron")

    def test_repr(self):
        """Test the repr method."""
        cq1 = CircularQueue()
        p1 = Process("john", 5)
        p2 = Process("bob", 10)
        p3 = Process("ron", 15)

        cq1.add_process(p1)
        cq1.add_process(p2)
        cq1.add_process(p3)

        expected_repr = "CircularQueue(Process(john,5), Process(bob,10), Process(ron,15))"
        self.assertEqual(repr(cq1), expected_repr)

    def test_remove_process(self):
        """Test the removal from the CircularQueue."""
        cq1 = CircularQueue()
        p1 = Process("john", 5)
        p2 = Process("bob", 10)
        p3 = Process("ron", 15)

        cq1.add_process(p1)
        cq1.add_process(p2)
        cq1.add_process(p3)

        cq1.remove_process(p2)
        self.assertEqual(len(cq1), 2)
        self.assertNotIn("bob", cq1._d_processes)  
        self.assertEqual(cq1._head.link.pid, "ron")

        cq1.remove_process(p1)
        self.assertEqual(len(cq1), 1)
        self.assertEqual(cq1._head.pid, "ron")

    def test_kill(self):
        """Test the kill functionality."""
        cq1 = CircularQueue()
        p1 = Process("john", 5)
        p2 = Process("bob", 10)
        p3 = Process("ron", 15)
        cq1.add_process(p1)
        cq1.add_process(p2)
        cq1.add_process(p3)
        killed_process = cq1.kill("bob")
        self.assertEqual(killed_process.pid, "bob") 
        self.assertEqual(len(cq1), 2)
        self.assertNotIn("bob", cq1._d_processes)

    def test_run(self):
        """Test running the CircularQueue for a specified number of cycles."""
        cq1 = CircularQueue()
        p1 = Process("john", 2)
        p2 = Process("bob", 3)
        p3 = Process("ron", 1)

        cq1.add_process(p1)
        cq1.add_process(p2)
        cq1.add_process(p3)

        result = cq1.run(4)

        self.assertIn("ron finished after 3 computational cycles.", result)


if __name__ == '__main__':
    unittest.main()