class Node:
    def __init__(self, value: int, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

    def __str__(self):
        return str(self.value)

def greatest_node(root: Node) -> int:
    if root is None:
        return float('-inf')
    
    left_greatest = greatest_node(root.left_child)
    right_greatest = greatest_node(root.right_child)

    return max(root.value, left_greatest, right_greatest)

# Test case
if __name__ == "__main__":
    tree = Node(2,
                left_child=Node(3,
                                left_child=Node(5),
                                right_child=Node(8)),
                right_child=Node(4,
                                 right_child=Node(11)))

    print(greatest_node(tree))  # Output: 11
