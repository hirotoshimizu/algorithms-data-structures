
from typing import Optional, Self


class TreeNode:
    def __init__(self, val: int, left: Optional[Self] = None, right: Optional[Self] = None) -> None:
        self.val = val
        self.left = left
        self.right = right

def preorder(root: TreeNode) -> None:
    cur = root
    stack: list[Optional[TreeNode]] = []
    res: list[int] = []

    while cur or stack:
        if cur:
            res.append(cur.val)
            stack.append(cur.right)
            cur = cur.left
        else:
            cur = stack.pop()
    
    for i in res:
        print(i)

if __name__ == "__main__":
    root = TreeNode(1)
    left_child_node = TreeNode(3)
    right_child_node = TreeNode(4)
    root.left = TreeNode(2, left_child_node, right_child_node)
    root.right = TreeNode(5)
    preorder(root)