
def sort_by_apparitions(crimes, seted_list):
    ocorrences = {}

    # set a dict as {number_of_ocorrence: [articles_with_this_number_of_appereance]}
    for article in crimes:
        count = crimes.count(article)
        if count not in ocorrences:
            ocorrences[count] = [article]
        else: ocorrences[count].append(article)

    # set a list with the number of appearances in descending order
    times = list(ocorrences.keys())
    times.sort(reverse=True)

    # make the output
    for number_of_ocorrence in times:
        ocorrences[number_of_ocorrence].sort(reverse=True)
        for article in seted_list:
            if article in ocorrences[number_of_ocorrence]:
                print(f'- Art. {article}: {number_of_ocorrence} ocorrencia(s).')


n = int(input())
suspects = {}
storage = []

for i in range(n):
    redneck, law = input().split()
    law = int(law)
    if( redneck not in suspects): suspects[redneck] = [law]
    else: suspects[redneck].append(law)

    storage.append(law)

stop = input().split()
for char in stop: 
    if char.isnumeric(): mount = char

# unsed line
trash_line = input()

# purge all the duplicates
seted_list = list(set(storage))
# reverse sorted list
seted_list.sort()


for i in range(int(mount)):
    suspect = input()

    if(suspect in suspects):
        print(f'Teje preso, {suspect}!')        
        crimes = suspects[suspect]
        sort_by_apparitions(crimes, seted_list)

    else:
        print(f'Grato, cidadao {suspect}.')
