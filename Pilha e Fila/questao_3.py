# frente: esquerda // fim: direita
class Queu:
    def __init__(self):
        self.fila = []

    def isEmpty(self):
        return self.items == []

    def insere(self, item):
        self.fila.append(item)
      
    def pop(self):
        return self.fila.pop(0)
      
    def peek(self):
        return self.fila[0]

    def bottom(self):
        return self.fila[-1]

    def size(self):
        return len(self.fila)

    def __str__(self):
        for elemento in self.fila: print(elemento)
        return ""

entrada = input().split()
times = int(input())
fila = Queu()

for nome in entrada: fila.insere(nome)

for i in range(times):
    fila.insere(fila.pop())

print("Pessoa da frente:", fila.peek())
print("Pessoa do fim:", fila.bottom())