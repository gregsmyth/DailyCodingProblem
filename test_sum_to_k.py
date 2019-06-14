import unittest
from sum_to_k import sum_to_k

class sum_to_k_TestCase(unittest.TestCase):
    """Tests for `sum_to_k.py`."""

    def test_given_example(self):
       self.assertTrue(sum_to_k([10,15,3,7], 17))

    def test_bad_example(self):
       self.assertFalse(sum_to_k([11,15,3,7], 17))
       
    def test_emptylist(self):
       self.assertFalse(sum_to_k([], 17))

    def test_zeros(self):
       self.assertTrue(sum_to_k([0], 0))
       
if __name__ == '__main__':
    unittest.main()
    

