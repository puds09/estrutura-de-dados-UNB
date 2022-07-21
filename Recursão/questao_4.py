def fib(n):
    if(n == 0):
        return n
    elif(n == 1):
        return n
    else:
        return fib(n-1) + fib(n-2)

def fibonacci(n):
    storage = []
    if(n == 0):
        return []
    else:
        for i in range(n):
            storage.append(fib(i))
        return storage

