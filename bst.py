class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return TreeNode(value)
    
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    
    return root

def height(root):
    if root is None:
        return 0
    else:
        return max(height(root.left), height(root.right)) + 1

def draw_bst(root, level=0):
    if root is not None:
        draw_bst(root.right, level + 1)
        print("    " * level + str(root.value))
        draw_bst(root.left, level + 1)

# Given data
values = [5, 7, 9, 2, 6, 11, 17]

# Construct the BST
bst_root = None
for value in values:
    bst_root = insert(bst_root, value)

# Calculate the height of the BST
bst_height = height(bst_root)

# Draw the BST
print("Binary Search Tree:")
draw_bst(bst_root)

# Print the height of the BST
print("\nHeight of the Binary Search Tree:", bst_height)
