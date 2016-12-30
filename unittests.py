import unittest
from tree import Node

class TestNode(unittest.TestCase):

    def test_insert(self):
        n = Node()
        n.add_record("foo")
        self.assertEqual(1, n.count_of_records())

    def test_delete(self):
        test_value = "foo"
        retained_value = "bar"
        n = Node()
        n.add_record(test_value)
        n.add_record(retained_value)
        self.assertEqual(2, n.count_of_records())
        n.remove_record(test_value)
        self.assertEqual(n.records, [retained_value])
        self.assertEqual(1, n.count_of_records())

if __name__ == '__main__':
    unittest.main()
