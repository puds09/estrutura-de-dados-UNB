
class Lista:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def set(self, pos,  item):
        self.items[pos] = item

    def get(self, pos):
        return self.items[pos]

    def remove(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __str__(self) -> str:
        for i in self.items: print(i, end=" ")
        return ""

# size, amount = input().split()

size, amount = [int(x) if x.isnumeric() else x for x in input().split()]

if amount != 0: datas = [int(x) if x.isnumeric() else x for x in input().split()]

tabela = Lista()
for i in range(size): tabela.add("[X]")

if amount != 0:
    for data in datas:
        resto = data % size #posição
        tabela.set(resto, [data]) if(tabela.get(resto) == "[X]") else tabela.get(resto).append(data)


for i in range(size):
    value = tabela.get(i)
    if value == "[X]":
        print(f'{i} - [x]') 
    
    else: 
        for indice in range(len(value)): 
            print(f'{i} - {value[indice]}',  end="") if indice == 0 else print(f' -> {value[indice]}',  end="")
        else:
            print()
# for i in range(tabela.size()): print(tabela.get(i))
