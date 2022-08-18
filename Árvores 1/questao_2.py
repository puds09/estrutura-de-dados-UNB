def mostra(raiz):

    print('(', end="")
    if(raiz == None): 
        print(")", end="")
        return

    print(raiz.dado, end=" ")

    mostra(raiz.esq)
    print(" ", end="")

    mostra(raiz.dir)
    print(")", end="")    
    