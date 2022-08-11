import math

n = int(input())

# store a list with the number of persons
storage = {}
# store all the averages
my_list = []

for i in range(n):
    mount, spent = input().split()
    mount, spent = [int(mount), int(spent)]

    if(mount != 0):
        average = math.ceil(spent/mount)
    else:
        average = 0

    # build the dict to get the amount later
    if(average in storage):
        storage[average].append(mount)
    else:
        storage[average] = [mount]

    my_list.append(average)

# purge all the duplicates
list_seted = list(set(my_list))

# reverse sorted list
list_seted.sort(reverse=True)


# make the output
for average in list_seted:
    storage[average].sort()
    for current in storage[average]:
        print(f'{average} / {current}')