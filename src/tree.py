class TreeAlgorithms:
    def __init__(self):
        self.curr_node = None
        self.tree = None

    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def create_sample_tree(self):
        self.tree = self.Node(5)
        self.tree.left = self.Node(30)
        self.tree.right = self.Node(70)
        self.tree.left.left = self.Node(20)
        self.tree.left.right = self.Node(40)
        self.tree.right.left = self.Node(60)
        self.tree.right.right = self.Node(80)
        return self.tree

    def inorder_traversal(self, node):
        pass

    def preorder_traversal(self, node):
        pass

    def postorder_traversal(self, node):
        pass
