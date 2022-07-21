
counter = []

def fibonacci(n):

    global counter

    counter[n] += 1

    if(n == 0):
        return n
    elif(n == 1):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input())

for i in range(n+1):
    counter.append(0)

result = fibonacci(n)

print(f'fibonacci({n}) = {result}.')

for i in range(n+1): print(f'{counter[i]} chamada(s) a fibonacci({i}).')
