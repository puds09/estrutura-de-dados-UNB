
def height(root):
    if(root is None): return -1

    leftHeight = height(root.esq)
    rigthHeight = height(root.dir)

    return max(leftHeight, rigthHeight) + 1

def show(raiz, prefixo):

    if raiz is None: return
    if raiz.dado: print(prefixo*"__", raiz.dado, sep="" )
    if raiz.dir is not None: show(raiz.dir, prefixo+1)
    if raiz.esq is not None: show(raiz.esq, prefixo+1)


def mostra_arvore_e_altura(raiz):
    show(raiz,  0)
    print()
    print("altura:", height(raiz)) if raiz is not None else print("altura: 0")

