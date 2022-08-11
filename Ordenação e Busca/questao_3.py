
def selection_sort(lista):
    for i in range(len(lista)-1):        
        menor = i
        for j in range(i, len(lista)):
            if lista[menor][1] >= lista[j][1]:
                lista[menor], lista[j]= lista[j], lista[menor] 

    return lista

def formating_time(time_in_float):
    min = time_in_float//60000
    sec_temp = (time_in_float/60000-min)*60
    sec = int(sec_temp)
    mm = (sec_temp - sec)*1000

    time = f'{int(min):0>1}:{int(sec):0>2}.{round(mm):0>3}'
    return time

n = int(input())
dict = {}
for i in range(n):
    name = input()
    laps = [x for x in input().split()]

    for i, lap in enumerate(laps):
        sec,  mm = lap.split(".")
        laps[i] = float(sec)*1000 + float(mm)        

    dict[name] = sum(laps)

sorted_pilots = selection_sort(list(dict.items()))

for i, pilot in enumerate(sorted_pilots):
    time_formated = formating_time(dict[pilot[0]])
    print(f'{i+1}. {pilot[0]} ({time_formated})')

