
def verifica(expressao):
    simbolo = ''
    dics = {'(':')', '[':']', '{':'}'}
    operators = ['+', '-', '*', '/']
    for i in range(len(expressao)):
        if(expressao[i] in dics.keys()):
            simbolo = expressao[i]
            if(expressao[i+1] == simbolo): # se após encontrar uma abertura o próximo char é igual essa abertura
                temp = expressao[i+2:]
                flag = False # liga quando encontrou um fechamento do current char
                cont = 0 # conta quantos operadores tem entre uma 2 aberturas e fechamentos de separadores
                for j in range(len(temp)):
                    if(temp[j] == simbolo):
                        if(abriuNoMeio(temp[j:])): continue
                        else: break

                    if (flag and temp[j] == dics[simbolo]):
                        return True
                    else: flag = False
                    
                    if(temp[j] == dics[simbolo]):
                        flag = True
    else: return False

#vai verificar se existe um operador dentro de um nova abertura enquanto está procurando 2 fechamentos consecutivos
def abriuNoMeio(operacao):
    dics = {'(':')', '[':']', '{':'}'}
    operators = ['+', '-', '*', '/']
    for i in range(len(operacao)):
        if(operacao[i] in dics.values()):
            return True
        if(operacao[i] in operators):
            return False

""" sequencia de linhas para produção do código """

# paramentro = []
# # entrada = "(1/2+3)+{6-((9/1)+3+(5*6))+[(1/2)+3+(4*5)]}"
# entrada = "((51)-14-12)"
# numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# # print(entrada)
# for i in entrada: 
#     if i not in numeros: paramentro.append(i)
# # print(*paramentro)
# print(verifica(paramentro))


""" sequencia de linhas para rodar o resultado final """

times = int(input())
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for i in range(times):
    paramentro = []
    entrada = input()
    for i in entrada: 
        if i not in numeros: paramentro.append(i)

    if(verifica(paramentro)):
        print("A expressão possui duplicata.")
    else:
        print("A expressão não possui duplicata.")