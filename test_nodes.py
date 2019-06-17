import unittest
from nodes import Node, serialize, deserialize

class nodes_TestCase(unittest.TestCase):
    """Tests for `nodes.py`."""

    def test_node(self):
       node = Node('root', Node('left', Node('left.left')), Node('right'))
       self.assertTrue(deserialize(serialize(node)).left.left.val == 'left.left')
       self.assertTrue(deserialize(serialize(node)).left.val == 'left')
       
if __name__ == '__main__':
    unittest.main()
    
