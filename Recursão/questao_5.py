def fat(n):
    result = 1
    if(n == 0):
        result = 1
        print(result, end=" ")
        return result
    elif(n < 7): # result smaller than 2357 (as ordered)
        result = n * fat(n-1)
        print(result, end=" ")
        return result
    else:
        result = (n * fat(n-1))%2357
        print(result, end=" ")
        return result


n = int(input())
for i in range(n):
    parameter = int(input())
    fat(parameter)
    print()