class node:
    # constructor
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val


def minimax(node, depth, isMax):
    if depth == 0:
        return node.value

    if isMax:
        bestValue = -1000000

        v = minimax(node.left, depth - 1, False)
        bestValue = max(bestValue, v)

        v = minimax(node.right, depth - 1, False)
        bestValue = max(bestValue, v)

        return bestValue

    else:
        bestValue = 10000000

        v = minimax(node.left, depth - 1, True)
        bestValue = min(bestValue, v)

        v = minimax(node.right, depth - 1, True)
        bestValue = min(bestValue, v)

        return bestValue


tree = node(0)
tree.left = node(0)
tree.right = node(0)

tree.left.left = node(0)
tree.left.right = node(0)

tree.left.left.left = node(1)
tree.left.left.right = node(3)

tree.left.right.left = node(5)
tree.left.right.right = node(1)

tree.right.left = node(0)
tree.right.right = node(0)

tree.right.left.left = node(6)
tree.right.left.right = node(4)

tree.right.right.left = node(0)
tree.right.right.right = node(9)

print(minimax(tree, 3, True))