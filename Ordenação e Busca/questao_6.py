n = int(input())

registers = []
for i in range(n): registers.append(input())
registers.sort()

count = 0
for i in range(len(registers)-1):
    for j in range(len(registers[i])):
        if(registers[i][j] == registers[i+1][j]): count += 1

print(f'R$ {count*0.07:.2f}')    
