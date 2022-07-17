from collections import deque

entrada = input()
dq = deque()


for char in entrada:
    if(char in ['*', '+']):
        if(char == '*'):
            print(dq.popleft(), end="")
        elif(char == '+'):
            print(dq.pop(), end="")

    elif(char.isdigit()):
        dq.append(char)
    else:
        dq.appendleft(char) 
