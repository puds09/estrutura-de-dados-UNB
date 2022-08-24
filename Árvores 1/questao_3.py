import re

def getElementById(raiz, id):

    temp = []
    for element in raiz:

        if id[0] == "*":
            match = re.findall(f'(.*{id[1:]}.*)|(.*{id[1:].upper()}.*)', element)
            if match: temp.append(element)

        elif id[-1] == "*":
            match = re.findall(f'(.*{id[:-1]}.*)|(.*{id[:-1].upper()}.*)|(.*{id[:-1].lower()}.*)', element)
            if match: temp.append(element)

        elif element == id :
            temp.append(element)

        if type(raiz[element]) is not str: temp += getElementById(raiz[element], id)


    return temp


#casos resolvidos:
# 1°
# raiz = {'HTML': {'HEAD': {'TITLE': 'Título'},'BODY': {'H1': 'header', 'P': 'Lorem', 'Y': 'ipsum'}}}
# print(sorted(getElementById(raiz, '*Y')))
# Output: ['BODY', 'Y']

# 2°
# raiz = {'H1': {'H2': {'H3': {'H4': {'H5': {'h1' : 'header', 'h2': 'outro', 'h3': 'hello', 'h4': 'world'}}}}}, 'H2': {'H1': 'H1', 'H2': 'H2', 'H3': 'H3', 'H4': 'H4', 'H5': 'H5'}} 
# print(sorted(getElementById(raiz, 'H*')))
# Output: ['H1', 'H1', 'H2', 'H2', 'H2', 'H3', 'H3', 'H4', 'H4', 'H5', 'H5', 'h1', 'h2', 'h3', 'h4']