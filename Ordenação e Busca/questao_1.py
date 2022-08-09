# I won't use this variable, but i need to create it because was ordered
n = int(input())
clothes = input().split()

duplicated = [clothe for i, clothe in enumerate(clothes) if i != clothes.index(clothe)]
print(len(duplicated))