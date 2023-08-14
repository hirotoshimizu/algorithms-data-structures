from typing import Optional, Self


class TreeNode:
    def __init__(self, val: Optional[int], left: Optional[Self] = None, right: Optional[Self] = None) -> None:
        self.val = val
        self.left = left
        self.right = right

def postorder(root: TreeNode) -> None:
    stack: list[Optional[TreeNode]] = [root]
    visited = [False]
    res: list[Optional[int]] = []

    while stack:
        cur, v = stack.pop(), visited.pop()
        
        if cur:
            if v:
                res.append(cur.val)
            else:
                stack.append(cur)
                visited.append(True)
                stack.append(cur.right)
                visited.append(False)
                stack.append(cur.left)
                visited.append(False)
        
    for i in res:
        print(i)
        


if __name__ == "__main__":
    root = TreeNode(1)
    left_child_node = TreeNode(3)
    right_child_node = TreeNode(4)
    root.left = TreeNode(2, left_child_node, right_child_node)
    root.right = TreeNode(5)

    postorder(root)