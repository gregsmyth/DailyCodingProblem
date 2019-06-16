import unittest
from product_exclude_current import product_exclude_current_easy, product_exclude_current_hard

class product_exclude_current_TestCase(unittest.TestCase):
    """Tests for `product_exclude_current.py`."""

    def test_given_example1(self):
       self.assertEqual(product_exclude_current_easy([1, 2, 3, 4, 5]), [120, 60, 40, 30, 24])
       self.assertEqual(product_exclude_current_hard([1, 2, 3, 4, 5]), [120, 60, 40, 30, 24])
       
    def test_given_example2(self):
       self.assertEqual(product_exclude_current_easy([3, 2, 1]), [2, 3, 6])
       self.assertEqual(product_exclude_current_hard([3, 2, 1]), [2, 3, 6])

       
if __name__ == '__main__':
    unittest.main()
