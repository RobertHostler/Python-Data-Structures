class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def add(self, current, value):
        if self.root == None:
            self.root = Node(value)
        else:
            if value < current.value:
                if current.left == None:
                    current.left = Node(value)
                else:
                    self.add(current.left, value)

            else:
                if current.right == None:
                    current.right = Node(value)
                else:
                    self.add(current.right, value)
    
    def visit(self, node):
        return node.value

    def preorder(self, current):
        self.visit(current)
        self.preorder(current.left)
        self.preorder(current.right)

    def inorder(self, current):
        self.inorder(current.left)
        self.visit(current)
        self.inorder(current.right)

    def postorder(self, current):
        self.postorder(current.left)
        self.postorder(current.right)
        self.visit(current)
