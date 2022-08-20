import re

def getElementById(raiz, id):

    temp = []
    for element in raiz:

        if id[0] == "*":
            match = re.findall(f'(.*{id[1:]}.*)|(.*{id[1:].upper()}.*)', element)
            if match: temp.append(element)

        elif id[-1] == "*":
            match = re.findall(f'(.*{id[:-1]}.*)|(.*{id[:-1].upper()}.*)', element)
            if match: temp.append(element)

        elif element == id :
            temp.append(element)

        if type(raiz[element]) is not str: temp += getElementById(raiz[element], id)


    return temp

#caso resolvido:
# raiz = {'HTML': {'HEAD': {'TITLE': 'Título'},'BODY': {'H1': 'header', 'P': 'Lorem', 'Y': 'ipsum'}}}
# print(sorted(getElementById(raiz, '*Y')))
 	