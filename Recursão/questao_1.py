def fibonacci(n):
    if(n == 0):
        return n
    elif(n == 1):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
