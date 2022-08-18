class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = int(data)

    def insert(self, data):
    # Compare the new value with the parent node
        data = int(data)
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

class binaryTree:

    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._add(data, self.root)
    
    def _add(self, data, node):
        data = int(data)
        if data < node.data:
            if node.left is not None:
                self._add(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right is not None:
                self._add(data, node.right)
            else:
                node.right = Node(data)

    def height(self, root):
        if(root is None): return -1

        leftHeight = self.height(root.left)
        rigthHeight = self.height(root.right)

        return max(leftHeight, rigthHeight) + 1


# MAIN
n = int(input())
# initialize a BinaryTree
binaryTree = binaryTree()

# Set the Tree
for data in input().split(): binaryTree.add(data)

# Show the output
print(binaryTree.height(binaryTree.getRoot()))
