class ArvoreBinaria():

    def __init__(self, dado, esq = None, dir = None):
        self.dado = dado
        self.esq = esq
        self.dir = dir

    def __str__(self):
        return f'{self.dado} -> ({self.esq}, {self.dir})'
        # pass

def constituiArvoreBinariaDeBusca(root):
    if root is None: return

    if(root.esq is not None):
        if root.dado < root.esq.dado: return False
        next = constituiArvoreBinariaDeBusca(root.esq)
        if not next: return False

    if(root.dir is not None):
        if root.dado > root.dir.dado: return False
        next = constituiArvoreBinariaDeBusca(root.dir)
        if not next: return False

    return True

raiz = ArvoreBinaria(7, ArvoreBinaria(4), ArvoreBinaria(10, ArvoreBinaria(11), ArvoreBinaria(15)))
print(constituiArvoreBinariaDeBusca(raiz))
