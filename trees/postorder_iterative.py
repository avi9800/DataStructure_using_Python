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

def postorder_iterative(root):
    if root is None:
        return
    
    stack1 = deque()
    stack2 = deque()

    node = root
    stack1.append(node)

    while stack1:
        item = stack1.pop()
        stack2.append(item)
        if item.left:
            stack1.append(item.left)
        if item.right:
            stack1.append(item.right)
    
    for i in range(len(stack2)-1,-1,-1):
        print(stack2[i].val,end=' ')
        



postorder_iterative(root)
    



