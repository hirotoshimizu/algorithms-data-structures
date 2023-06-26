class Node:
    def __init__(self, value: int) -> None:
        self.left = None
        self.right = None
        self.value = value


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    root.left.left = Node(4)

    print(root.value)
    print(root.left.value)
    print(root.right.value)
    print(root.left.left.value)
