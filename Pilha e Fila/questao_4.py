# topo: esquerda // bottom: direita
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)
      
    def pop(self):
        return self.items.pop(0)
      
    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

    def __str__(self):
        for elemento in self.items: print(elemento)
        return ""


stack = Stack()
while(True):
    entrada = int(input())
    if(entrada == 0):
        break
    stack.push(entrada)

desejado = int(input())
count = 0
retirado = []
while(True):
    if (stack.isEmpty() == False): retirado.append(stack.pop())
    else: 
        print("Peso retirado: 0")
        break
    print("Peso retirado:", retirado[-1])
    count += 1

    if(retirado[-1] == desejado):
        break

print("Anilhas retiradas:", count)
print("Peso total movimentado:", sum(retirado))