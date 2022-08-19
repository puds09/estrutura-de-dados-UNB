
# class ArvoreBinaria():

#     def __init__(self, dado, esq = None, dir = None):
#         self.dado = dado
#         self.esq = esq
#         self.dir = dir

def show(root, prefixo):

    if root is None: return
    if root.dado: print(prefixo*"__", root.dado, sep="" )
    if root.dir is not None: show(root.dir, prefixo+1)
    if root.esq is not None: show(root.esq, prefixo+1)

def nivel(root, data):

    global height
    global next
    if root is None: return 

    if root.dado == data: return height
    if root.dir is not None: 
        height += 1
        next = nivel(root.dir, data)
        height -= 1
        if str(next).isnumeric(): 
            return next


    if root.esq is not None:
        height += 1
        next = nivel(root.esq, data)
        height -= 1
        if str(next).isnumeric(): 
            return next


height = 0
next = -1

def mostra_arvore_e_nivel(root, data):
    show(root, 0)
    print("")
    output = nivel(root, data)
    #just build the output
    print(f'nivel(raiz, {data}): {output}') if str(output).isnumeric() else print(f'nivel(raiz, {data}): -1')


# root = ArvoreBinaria(7, ArvoreBinaria(4), ArvoreBinaria(10, ArvoreBinaria(11), ArvoreBinaria(15)))
# data = 10
# mostra_arvore_e_nivel(root, data)