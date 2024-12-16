import unittest
# Include unittests here. Focus on readability, including comments and docstrings.
from RecordsMap import RecordsMap 
from RecordsMap import LocalRecord 

class TestLocalRecord(unittest.TestCase):
    def test_init(self):
        """Test initializing LocalRecord with position and temperature limits."""
        record = LocalRecord((41.8067, -72.2522))
        self.assertEqual(record.pos, (42, -72))  # Default precision rounding

    def test_hash(self):
        """Test hash generation for LocalRecord based on position."""
        record = LocalRecord((41.8067, -72.2522))
        self.assertEqual(hash(record), hash((42, -72)))

    def test_eq(self):
        """Test equality comparison between two LocalRecords."""
        record1 = LocalRecord((41.8067, -72.2522))
        record2 = LocalRecord((41.8067, -72.2522))
        self.assertEqual(record1, record2)

    def test_add_report(self):
        """Test adding temperature reports to update max and min."""
        record = LocalRecord((41.8067, -72.2522))
        record.add_report(25)
        self.assertEqual(record.max, 25)
        self.assertEqual(record.min, 25)
        record.add_report(30)
        self.assertEqual(record.max, 30)
        self.assertEqual(record.min, 25)
        record.add_report(20)
        self.assertEqual(record.min, 20)


class TestRecordsMap(unittest.TestCase):
    def test_add_one_report(self):
        """Test adding one report"""
        rm = RecordsMap()
        rm.add_report((41.8067, -72.2522), 25)
        self.assertEqual(len(rm), 1)
        self.assertIn((41.8067, -72.2522), rm)
        self.assertEqual(rm[(41.8067, -72.2522)], (25, 25))

    def test_add_many_reports(self):
        """Test adding multiple reports"""
        rm = RecordsMap()
        rm.add_report((41.8067, -72.2522), 25)
        rm.add_report((41.8097, -72.1473), 30)
        rm.add_report((41.8067, -72.2522), 20)  
        self.assertEqual(len(rm), 1)
        self.assertIn((41.8067, -72.2522), rm)
        self.assertIn((41.8097, -72.1473), rm)
        self.assertEqual(rm[(41.8067, -72.2522)], (20, 25))
        self.assertEqual(rm[(41.8097, -72.1473)], (30, 30))

# You need to add a line here to run the unittests
if __name__ == "__main__":
    unittest.main()