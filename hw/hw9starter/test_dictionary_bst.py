import unittest
from dictionary_bst import DictionaryBST

class TestDictionaryBST(unittest.TestCase):

    def setUp(self):
        self.dictionary = DictionaryBST()
        self.dictionary.insert("banana", "A yellow tropical fruit.")
        self.dictionary.insert("apple", "A fruit that grows on trees.")
        self.dictionary.insert("cherry", "A small, round, red fruit.")

    def test_insert_and_search(self):
        self.dictionary.insert("date", "A sweet, dark fruit.")
        self.assertEqual(self.dictionary.search("date"), "A sweet, dark fruit.")
        self.assertEqual(self.dictionary.search("banana"), "A yellow tropical fruit.")
        self.assertIsNone(self.dictionary.search("kiwi"))

    def test_update_existing_word(self):
        self.dictionary.insert("banana", "A yellow fruit with soft flesh.")
        self.assertEqual(self.dictionary.search("banana"), "A yellow fruit with soft flesh.")

    def test_print_alphabetical(self):
        expected_output = [
            ("apple", "A fruit that grows on trees."),
            ("banana", "A yellow tropical fruit."),
            ("cherry", "A small, round, red fruit.")
        ]
        self.assertEqual(self.dictionary.print_alphabetical(), expected_output)

if __name__ == "__main__":
    unittest.main()