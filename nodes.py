""" Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
 """
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node = Node('root', Node('left', Node('left.left')), Node('right'))

def serialize(node):
    serial = ""
    serial = serial + node.val
    if (node.left is not None):
        serial = serial + ', ' + serialize(node.left)
    else:
        serial = serial + ', None'
    if (node.right is not None):
        serial = serial + ', ' + serialize(node.right)
    else:
        serial = serial + ', None'
    return serial


def deserialize(node_string):
    x = node_string.split(', ')
    if x[0] == 'None':
        return None
    node = Node(x[0])
    new_node_string = ', '
    node.left = deserialize(new_node_string.join(x[1:]))
    node.right = deserialize(new_node_string.join(x[1:]))
    return node

