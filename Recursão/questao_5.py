def fat(n):
    result = 1
    if(n == 0):
        result = 1
        print(result, end=" ")
        return result
    else:
        print(1, end=" ")
        for i in range(1, n+1):
            result *= i
            result %= 2357
            print(result, end=" ")
        return result


n = int(input())
for i in range(n):
    parameter = int(input())
    fat(parameter)
    print()