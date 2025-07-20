# Tree Creation
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

arr = ['A', 'B', 'C', 'D', 'E','F','G', 'H', 'I','J','K','L','M','N','O']



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

from collections import deque

def zigzag(node):
    if node == None:
        return

    queue = deque()
    queue.append(node)
    Direction = 'L'
    temp = deque()
    print(node.val,end=' ')
    while queue:
        if Direction == 'L':
            while queue:
                item = queue.pop()
                if item.left is not None:
                    temp.append(item.left)
                    print(item.left.val, end=' ')
                if item.right is not None:
                    temp.append(item.right)
                    print(item.right.val, end=' ')
            Direction = 'R'
            queue = temp.copy()
            temp = deque()
        if Direction == 'R':
            while queue:
                item = queue.pop()
                if item.right is not None:
                    temp.append(item.right)
                    print(item.right.val, end=' ')
                if item.left is not None:
                    temp.append(item.left)
                    print(item.left.val, end=' ')
            Direction = 'L'
            queue = temp.copy()
            temp = deque()

zigzag(root)


