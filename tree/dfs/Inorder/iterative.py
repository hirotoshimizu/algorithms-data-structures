from typing import Optional, Self


class TreeNode:
    def __init__(self, val: int, left: Optional[Self] = None, right: Optional[Self] = None) -> None:
        self.val = val
        self.left = left
        self.right = right

def inorder(root: Optional[TreeNode]) -> None:
    res: list[TreeNode] = []
    stack: list[TreeNode] = []
    cur = root

    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        res.append(cur)
        cur = cur.right
    
    for i in res:
        print(i.val)


if __name__ == "__main__":
    root = TreeNode(1)
    left_child_node = TreeNode(3)
    right_child_node = TreeNode(4)
    root.left = TreeNode(2, left_child_node, right_child_node)
    root.right = TreeNode(5)
    inorder(root)