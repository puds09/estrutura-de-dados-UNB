entrada = input().split()
lista = []

while(entrada[0] != 'X'):
    if(entrada[0] == 'I'):
        lista.insert(0, entrada[1])
    elif(entrada[0] == 'F'):
        lista.append(entrada[1])
    elif(entrada[0] == 'P'):
        print(lista[-1])
        lista.pop()
    elif(entrada[0] == 'D'):
        print(lista[0])
        lista.pop(0)

    entrada = input().split()

for i in lista: print(i)