class Node:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None

def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.root, end=' ')
    inorder(node.right)

def pre_order(node):
    if node is None:
        return
    
    print(node.root, end=' ')
    pre_order(node.left)
    pre_order(node.right)

def post_order(node):
    if node is None:
        return
    
    post_order(node.left)
    post_order(node.right)
    print(node.root, end=' ')

arr = [1, 2, 3, 4, 5, 6, 7,8,9,10]

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

# Perform inorder traversal
print("Inorder")
inorder(root)

print("PreOrder")
pre_order(root)

print("PostOrder")
post_order(root)

