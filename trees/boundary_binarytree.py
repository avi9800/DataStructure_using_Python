# Tree Creation
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Create nodes
root = Node(10)
root.left = Node(5)
root.right = Node(20)

root.left.left = Node(3)
root.left.right = Node(8)
root.left.right.right = Node(9)

root.right.left = Node(15)
root.right.right = Node(25)
root.right.right.right = Node(30)

from collections import deque

def boundary(root):
    if root is None:
        return
    
    queue = deque()

    #Print the boundary left
    def left_boundary(node):
        while node.left or node.right:
            if node.left is not None:
                queue.append(node.val)
                node = node.left
            elif node.right is not None:
                queue.append(node.val)
                node = node.right
    
    left_boundary(root)
    
    #Print the leaf nodes
    def inorder(node):
        if node is None:
            return
        
        inorder(node.left)
        if node.left is None and node.right is None:
            queue.append(node.val)
        inorder(node.right)
    
    inorder(root)
    
    #Print the right nodes
    def right_boundary(node):
        if node.right is None and node.left is None:
            return
        
        if node.right is not None:
            right_boundary(node.right)
        elif node.left is not None:
            right_boundary(node.left)
        if node.right is not None or node.left is not None:
            queue.append(node.val)
    
    right_boundary(root)
    queue.pop()

    print(queue)

boundary(root)

          

