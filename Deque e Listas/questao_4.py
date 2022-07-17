import re

def regex(padrao, string):
    for i in range(len(string)):
        padrao += f'({string[i:]})|'
    if (len(string) > 1): 
        padrao = regex(padrao, string[:-1])
    return padrao

def conta_maior(sequences):
    maior = 0
    for i in range(len(sequences)):
        for j in range(len(sequences[i])):
            if(len(sequences[i][j]) > maior ): 
                maior = len(sequences[i][j])
    return maior

covid = input()
gripe = input()

print(len(covid))
print(len(gripe))

if(len(covid) > len(gripe)):
    padrao = regex("", gripe)
    maior = conta_maior(re.findall(padrao, r'[{}]'.format(covid)))
else:
    padrao = regex("", covid)
    maior = conta_maior(re.findall(padrao, r'[{}]'.format(gripe)))

print(maior)

