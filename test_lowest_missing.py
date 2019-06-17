import unittest
from lowest_missing import lowest_missing

class lowest_missing_TestCase(unittest.TestCase):
    """Tests for `lowest_missing.py`."""

    def test_given_example(self):
       self.assertEqual(lowest_missing([3, 4, -1, 1]), 2)

    def test_given_example2(self):
       self.assertEqual(lowest_missing([1, 2, 0]), 3)
       
if __name__ == '__main__':
    unittest.main()
