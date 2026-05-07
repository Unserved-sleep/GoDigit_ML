class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []

    def add_child(self, child):
        self.children.append(child)

class Tree:
    def __init__(self, root):
        self.root = root

    def dfs(self, node=None):
        if node is None:
            node = self.root
        print(node.val, end=' ')
        for child in node.children:
            self.dfs(child)


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

print("\nDFS Traversal:\n")
tree.dfs()