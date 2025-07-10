# Tree Creation
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

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

def BFS(root):
    if root == None:
        return
    
    queue = deque()
    
    #Adding root
    queue.append(root)
    while queue:
        #Print the parent
        parent = queue.popleft()
        print(parent.val, end=' ')

        #add left and right child to queue
        if parent.left is not None:
              queue.append(parent.left)
        if parent.right is not None:
              queue.append(parent.right)


BFS(root)
    



