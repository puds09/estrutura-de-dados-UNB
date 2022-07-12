# topo: esquerda // bottom: direita
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)
      
    def pop(self):
        self.items.pop(0)
      
    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

    def __str__(self):
        for elemento in self.items: print(elemento)
        return ""

entrada = input().split()

palavras = Stack()
numeros = Stack()
conjunto_numerico = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for var in entrada:
    if(var[0] in conjunto_numerico): 
        numeros.push(var) 
    else: 
        palavras.push(var)

print("Palavras:")
print(palavras)
print("Numeros:")
print(numeros)
