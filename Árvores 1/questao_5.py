
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

    # mode: "in" visualization
    def mostra_in(self, raiz):

        if(raiz == None): 
            return

        self.mostra_in(raiz.left)
        print(raiz.data, end=" ")
        self.mostra_in(raiz.right)


    # mode: "pre" visualization
    def mostra_pre(self, raiz):

        if(raiz == None): 
            return

        print(raiz.data, end=" ")
        self.mostra_pre(raiz.left)
        self.mostra_pre(raiz.right)


    # mode: "pos" visualization
    def mostra_pos(self, raiz):

        if(raiz == None): 
            return

        self.mostra_pos(raiz.left)
        self.mostra_pos(raiz.right)
        print(raiz.data, end=" ")
        


binaryTree = binaryTree()
n = input()

while(n != "quack"):
    root = binaryTree.getRoot()

    if(n.isnumeric()): 
        binaryTree.add(int(n))
    elif(n == "in"): 
        binaryTree.mostra_in(root)
        print()
    
    elif(n == "pre"): 
        binaryTree.mostra_pre(root)
        print()

    elif(n == "pos"): 
        binaryTree.mostra_pos(root)
        print()

    n = input()