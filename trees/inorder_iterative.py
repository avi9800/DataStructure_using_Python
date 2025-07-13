# Tree Creation
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

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

def in_order_iterative(root):
    if root is None:
        return
    
    stack = deque()
    node = root

    #Using FIFO of stack
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            print(node.val, end=' ')
            node = node.right
        
        



in_order_iterative(root)
    



