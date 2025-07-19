# Tree Creation
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

#arr = ['A', 'B', 'C', 'D', 'E']

# More unbalanced binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.left.left.left = Node(6)
root.left.left.left.left = Node(8)
root.left.left.left.left.left = Node(9)

root.right.right = Node(7)

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

#root = tree(arr) #Tree formed
#node = root


def height(node):
    if node is None:
        return 0
    
    lh = height(node.left)
    rh = height(node.right)

    return max(lh,rh)+1

def brute_force(node,d):
    if node is None:
        return
    lh = height(node.left)
    rh = height(node.right)
    d = max(d,lh+rh+1)
    
    brute_force(node.left,d)
    brute_force(node.right,d)
    return d

Diameter = [0]
def optimal(node,Diameter):
    if node is None:
        return 0
    
    lh = optimal(node.left,Diameter)
    rh = optimal(node.right,Diameter)
    Diameter[0] = max(Diameter[0], lh+rh+1)

    return max(lh,rh)+1

print(optimal(root,Diameter))
