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

def identical(nodeA, nodeB):
    if nodeA is None and nodeB is None:
        return True
    if nodeA is None or nodeB is None:
        return False
    if nodeA.val != nodeB.val:
        return False
    
    return identical(nodeA.left, nodeB.left) and identical(nodeA.right, nodeB.right)

if identical(root1, root2):
    print("Identical")
else:
    print("Not identical")
