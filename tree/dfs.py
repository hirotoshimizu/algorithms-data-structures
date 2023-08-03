from collections import deque


class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


def preorder(root):
    if not root:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)
    

def inorder(root):
    if not root:
        return
    preorder(root.left)
    print(root.val)
    preorder(root.right)


def postorder(root):
    if not root:
        return
    preorder(root.left)
    preorder(root.right)
    print(root.val)

if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(3)
    root.right = TreeNode(6)

    postorder(root)
