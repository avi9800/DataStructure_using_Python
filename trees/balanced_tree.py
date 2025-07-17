# Tree Creation
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

arr = ['A', 'B', 'C', 'D', 'E']

def tree(arr):
    # Create Node objects and store in list with dummy at index 0
    nodes = [None]  # 0th index is unused
    for val in arr:
        nodes.append(Node(val))

    # Link the nodes to form the binary tree
    for i in range(1, len(nodes)):
        if 2 * i < len(nodes):
            nodes[i].left = nodes[2 * i]
        if 2 * i + 1 < len(nodes):
            nodes[i].right = nodes[2 * i + 1]

    # The root of the tree is at index 1
    root = nodes[1]
    return root

root = tree(arr) #Tree formed
node = root

from collections import deque


def balanced_tree(node):
    if node == None:
        return 0
    
    lh = height(node.left)
    if lh == -1:
        return -1
    rh = height(node.right)
    if rh == -1:
        return -1
    if abs(lh-rh) > 1:
        return -1
    
    return max(lh,rh)+1


print(balanced_tree(root))
