
class Arvore():
    def __init__(self, dado):
        self.dado = dado
        self.filhos = []


def mostra(raiz, pre):
    global quantity

    if raiz is None: return
    if raiz.dado: print(pre*quantity, raiz.dado, sep="" )

    for i, filho in enumerate(raiz.filhos):
        if i == 0: quantity += 1
        mostra(filho, pre)
        if i == len(raiz.filhos)-1: quantity -= 1

quantity = 0
