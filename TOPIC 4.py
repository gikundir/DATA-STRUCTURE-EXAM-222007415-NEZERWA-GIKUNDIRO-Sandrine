class BinaryTreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = BinaryTreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if not node.left:
            node.left = BinaryTreeNode(key)
        elif not node.right:
            node.right = BinaryTreeNode(key)
        else:
            self._insert(node.left, key)

    def inorder(self, node):
        if not node:
            return []
        return self.inorder(node.left) + [node.key] + self.inorder(node.right)


bt = BinaryTree()
keys = [1, 2, 3, 4, 5]
for key in keys:
    bt.insert(key)

print("Inorder Traversal of Binary Tree:", bt.inorder(bt.root))
