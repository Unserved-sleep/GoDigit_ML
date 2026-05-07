class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)


class Tree:
    def __init__(self, root):
        self.root = root

    def find_lca(self, node, a, b):
        if node.value == a or node.value == b:
            return node

        matches = []
        for child in node.children:
            result = self.find_lca(child, a, b)
            if result:
                matches.append(result)

        if len(matches) >= 2:
            return node
        if len(matches) == 1:
            return matches[0]
        return None

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n8 = TreeNode(8)
n9 = TreeNode(9)

n1.add_child(n2)
n1.add_child(n3)
n1.add_child(n4)
n2.add_child(n5)
n2.add_child(n6)
n4.add_child(n7)
n7.add_child(n8)
n7.add_child(n9)

tree = Tree(n1)

print("Tree:\n")
tree.print_tree()

ancestor = tree.find_lca(tree.root, 8, 9)
print("\nLowest Common Parent:", ancestor.value)