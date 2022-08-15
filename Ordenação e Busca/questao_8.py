
def negative_modular():
    current = number
    module = k
    while(True):
        if(current + module > 0):
            break
        current += module

    return current

n, k = map(int, input().split())

storage = []
for i in range(n): 
    number = int(input())
    module = number % k if(number > 0) else negative_modular()
    odd = number % 2
    tuple = (module, -odd, -number if odd else number, number)
    
    storage.append(tuple)


for element in sorted(storage, reverse=True): print(element[-1], end=" ")


# # print(storage)
# storage.sort(reverse=True)
# # print(storage)


